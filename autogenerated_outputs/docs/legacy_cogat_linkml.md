
# legacy-cogat-linkml


**metamodel version:** 1.7.0

**version:** None


Linkml implementation of cognitive atlas.


### Classes

 * [AssertionCollection](AssertionCollection.md)
 * [BatteryCollection](BatteryCollection.md)
 * [BehaviorCollection](BehaviorCollection.md)
 * [CitationCollection](CitationCollection.md)
 * [ConceptClassCollection](ConceptClassCollection.md)
 * [ConceptCollection](ConceptCollection.md)
 * [ConditionCollection](ConditionCollection.md)
 * [ContrastCollection](ContrastCollection.md)
 * [DisambiguationCollection](DisambiguationCollection.md)
 * [DisorderCollection](DisorderCollection.md)
 * [ExternalDatasetCollection](ExternalDatasetCollection.md)
 * [ExternalLinkCollection](ExternalLinkCollection.md)
 * [ImplementationCollection](ImplementationCollection.md)
 * [IndicatorCollection](IndicatorCollection.md)
 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [CitableThing](CitableThing.md)
         * [Assertion](Assertion.md)
         * [Battery](Battery.md)
         * [Behavior](Behavior.md) - Represents a Task
         * [Citation](Citation.md)
         * [Concept](Concept.md) - Represents a Task
         * [ConceptClass](ConceptClass.md)
         * [Condition](Condition.md) - Represents a Task
         * [Contrast](Contrast.md) - Represents a Task
         * [Disambiguation](Disambiguation.md)
         * [Disorder](Disorder.md) - Represents a Task
         * [ExternalDataset](ExternalDataset.md)
         * [ExternalLink](ExternalLink.md)
         * [Implementation](Implementation.md)
         * [Indicator](Indicator.md)
         * [Task](Task.md) - Represents a Task
         * [Theory](Theory.md)
         * [Trait](Trait.md) - Represents a Task
         * [User](User.md)
 * [TaskCollection](TaskCollection.md) - A holder for Task objects
 * [TheoryCollection](TheoryCollection.md)
 * [TraitCollection](TraitCollection.md)
 * [UserCollection](UserCollection.md)

### Mixins


### Slots

 * [alias](alias.md)
 * [➞entries](assertionCollection__entries.md)
 * [asserts](asserts.md)
 * [➞entries](batteryCollection__entries.md)
 * [➞kind_of](battery__kind_of.md)
 * [➞part_of](battery__part_of.md)
 * [➞entries](behaviorCollection__entries.md)
 * [➞entries](citationCollection__entries.md)
 * [citation_authors](citation_authors.md)
 * [citation_comment](citation_comment.md)
 * [citation_desc](citation_desc.md)
 * [citation_pmid](citation_pmid.md)
 * [citation_pubdate](citation_pubdate.md)
 * [citation_pubname](citation_pubname.md)
 * [citation_source](citation_source.md)
 * [citation_type](citation_type.md)
 * [citation_url](citation_url.md)
 * [classification](classification.md)
 * [classified_under](classified_under.md)
 * [collection](collection.md)
 * [collection_alias](collection_alias.md)
 * [collection_date_introduced](collection_date_introduced.md)
 * [collection_description](collection_description.md)
 * [collection_publisher](collection_publisher.md)
 * [➞entries](conceptClassCollection__entries.md)
 * [➞entries](conceptCollection__entries.md)
 * [➞entries](conditionCollection__entries.md)
 * [condition_description](condition_description.md)
 * [condition_text](condition_text.md)
 * [confidence_level](confidence_level.md)
 * [➞entries](contrastCollection__entries.md)
 * [created](created.md)
 * [creation_time](creation_time.md)
 * [dataset_name](dataset_name.md)
 * [dataset_uri](dataset_uri.md)
 * [def_event_stamp](def_event_stamp.md)
 * [def_id](def_id.md)
 * [def_id_user](def_id_user.md)
 * [definition](definition.md)
 * [definition_text](definition_text.md)
 * [description](description.md) - A human-readable description for a thing
 * [disambiguates](disambiguates.md) - Could apply to Concepts, Tasks, Traits...
 * [➞entries](disambiguationCollection__entries.md)
 * [➞entries](disorderCollection__entries.md)
 * [display_order](display_order.md)
 * [doi](doi.md)
 * [event_stamp](event_stamp.md)
 * [➞entries](externalDatasetCollection__entries.md)
 * [➞entries](externalLinkCollection__entries.md)
 * [flag_for_curator](flag_for_curator.md)
 * [has_citation](has_citation.md)
 * [has_condition](has_condition.md)
 * [has_contrast](has_contrast.md)
 * [has_difference](has_difference.md)
 * [has_external_dataset](has_external_dataset.md)
 * [has_implementation](has_implementation.md)
 * [has_indicator](has_indicator.md)
 * [has_link](has_link.md)
 * [id](id.md) - A unique identifier for a thing
 * [id_concept_class](id_concept_class.md)
 * [id_protocol](id_protocol.md)
 * [id_subject_def](id_subject_def.md)
 * [id_task](id_task.md)
 * [id_term](id_term.md)
 * [id_user](id_user.md)
 * [➞entries](implementationCollection__entries.md)
 * [implementation_description](implementation_description.md)
 * [implementation_name](implementation_name.md)
 * [implementation_uri](implementation_uri.md)
 * [in_battery](in_battery.md)
 * [in_theory](in_theory.md)
 * [➞entries](indicatorCollection__entries.md)
 * [is_a](is_a.md)
 * [is_a_fulltext](is_a_fulltext.md)
 * [is_a_protocol](is_a_protocol.md)
 * [kind_of](kind_of.md)
 * [last_updated](last_updated.md)
 * [measured_by](measured_by.md)
 * [name](name.md) - A human-readable name for a thing
 * [old_user_id](old_user_id.md) - The original PHP based site had user ids of the pattern "usr_[[:alnum:]]*". If an id of this kind existed for the user it is stored here.
 * [part_of](part_of.md)
 * [predicate](predicate.md)
 * [predicate_def](predicate_def.md)
 * [review_status](review_status.md)
 * [subject](subject.md)
 * [➞entries](taskCollection__entries.md)
 * [➞kind_of](task__kind_of.md)
 * [➞part_of](task__part_of.md)
 * [➞entries](theoryCollection__entries.md)
 * [➞kind_of](theory__kind_of.md)
 * [➞part_of](theory__part_of.md)
 * [➞entries](traitCollection__entries.md)
 * [truth_value](truth_value.md)
 * [type](type.md)
 * [uri](uri.md)
 * [➞entries](userCollection__entries.md)
 * [user_id](user_id.md)
 * [username](username.md)
 * [website](website.md)

### Enums


### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
