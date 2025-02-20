'''
    Inputs to this contain and rely on data that can't be in a public repo.
'''
import json
from collections import defaultdict

import legacy_cogat_linkml.datamodel.legacy_cogat_linkml as cml
from linkml_runtime.dumpers import json_dumper

def load_js(file='./all_20250219.json'):
    nodes = []
    relationships = []
    with open(file, 'r') as fp:
        lines = fp.readlines()
    js = [json.loads(x) for x in lines]
    for entry in js:
        if entry['type'] == 'node':
            nodes.append(entry)
        elif entry['type'] == 'relationship':
            relationships.append(entry)
        else:
            print(f'Weired node type: {entry}')

    return nodes, relationships

'''
    The majority of the old data was in neo4j, but the original user ids used
    in the previous PHP/SQL iteration of the site were stored in a django
    user model. These older user ids should be represented to make the data
    interpretable.
'''
def load_old_ids(file='./old_ids.json'):
    users = {}
    with open(file, 'r') as fp:
        user_js = json.load(fp)
    for user in user_js:
        users[user['email']] = user['old_id']
    return users

old_ids = load_old_ids()

def normalize_node(node):
    term_type = node.get('labels', [None])[0]
    props = node.get('properties', {})
    
    if 'id' in props:
        props['id'] = str(props['id'])
    # Indicators don't have a name property, but the type field acts as one
    if term_type == 'indicator':
        if 'type' in props and 'name' not in props:
            props['name'] = props['type']
    if 'id' not in props:
        props['id'] = node['id']
    if term_type == 'user':
        if 'username' in props:
            if props['username'] in old_ids:
                props['old_user_id'] = old_ids[props['username']]
            del props['username']
        if 'name' in props and props['name'] != props['id']:
            if props['name'] in old_ids:
                props['old_user_id'] = old_ids[props['name']]
            props['name'] = props['id']

new_key_lookup = {
    'CLASSIFIEDUNDER': 'classified_under',
    'HASCITATION': 'has_citation',
    'HASCONDITION': 'has_condition',
    'HASCONTRAST': 'has_contrast',
    'HASDIFFERENCE': 'has_difference',
    'HASEXTERNALDATASET': 'has_external_dataset',
    'HASIMPLEMENTATION': 'has_implementation',
    'HASINDICATOR': 'has_indicator',
    'INBATTERY': 'in_battery',
    'INTHEORY': 'in_theory',
    'ISA': 'is_a',
    'KINDOF': 'kind_of',
    'MEASUREDBY': 'measured_by',
    'PARTOF': 'part_of',
    'PREDICATEDEF': 'predicate_def'
}

def add_relationship(new_terms, relationship):
    rel_type = relationship['label']
     
    start = new_terms.get(relationship['start']['id'])
    end = new_terms.get(relationship['end']['id'])

    rel_key = rel_type.lower()
    if rel_key not in start:
        rel_key = new_key_lookup.get(rel_type)
    if rel_key is None:
        raise Exception(f'{rel_type} not found for {start}')

    try:
        start[rel_key].append(end.id)
    except Exception as e:
        print(relationship)
        print(start)
        raise e
    
def generate_and_dump_term_collections(terms):
    collections = {}
    collection_names = [x for x in cml.__dict__.keys() if "Collection" in x]
    for name in collection_names:
        MlClass = getattr(cml, name)
        collections[name] = MlClass()
    for term in terms.values():
        collection_name = f'{term.class_name}Collection'
        try:
            collections[collection_name].entries.append(term)
        except Exception as e:
            print(collection_name)
            print(collections[collection_name])
            raise e
    for name, collection in collections.items():
        json_dumper.dump(collection, f'./data/{name}.json')
    return collections


if __name__ == '__main__':
    nodes, relationships = load_js()
    new_fields = [x for x in dir(cml.slots()) if not x.startswith('_')]
    new_term_instances = {}
    failed_terms = []

    term_types = defaultdict(set)
    for node in nodes:
        term_type = node.get('labels', [None])[0]
        normalize_node(node)
        props = node.get('properties', {})
        [term_types[term_type].add(x) for x in props]

        class_name = ''.join(x.title() for x in term_type.split('_'))
        MlClass = getattr(cml, class_name)
        try:
            ml_term = MlClass(**props)
            if node['id'] in new_term_instances:
                raise Exception(f"id: {node['id']} has multiple entries")
            new_term_instances[node['id']] = ml_term
        except ValueError as e:
            failed_terms.append((node, e))

    for rel in relationships:
        add_relationship(new_term_instances, rel)
    collections = generate_and_dump_term_collections(new_term_instances)
