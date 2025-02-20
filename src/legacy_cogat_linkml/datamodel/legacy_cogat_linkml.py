# Auto generated from legacy_cogat_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-02-20T10:02:11
# Schema: legacy-cogat-linkml
#
# id: https://w3id.org/rwblair/legacy-cogat-linkml
# description: Linkml implementation of cognitive atlas.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LEGACY_COGAT_LINKML = CurieNamespace('legacy_cogat_linkml', 'https://w3id.org/rwblair/legacy-cogat-linkml/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LEGACY_COGAT_LINKML


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class CitableThingId(NamedThingId):
    pass


class TaskId(CitableThingId):
    pass


class ConceptId(CitableThingId):
    pass


class DisorderId(CitableThingId):
    pass


class TraitId(CitableThingId):
    pass


class BehaviorId(CitableThingId):
    pass


class ConditionId(CitableThingId):
    pass


class ContrastId(CitableThingId):
    pass


class BatteryId(CitableThingId):
    pass


class TheoryId(CitableThingId):
    pass


class ImplementationId(CitableThingId):
    pass


class ExternalDatasetId(CitableThingId):
    pass


class IndicatorId(CitableThingId):
    pass


class CitationId(CitableThingId):
    pass


class AssertionId(CitableThingId):
    pass


class UserId(CitableThingId):
    pass


class ExternalLinkId(CitableThingId):
    pass


class ConceptClassId(CitableThingId):
    pass


class DisambiguationId(CitableThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CitableThing(NamedThing):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["CitableThing"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:CitableThing"
    class_name: ClassVar[str] = "CitableThing"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.CitableThing

    id: Union[str, CitableThingId] = None
    has_citation: Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]] = empty_list()
    last_updated: Optional[str] = None
    creation_time: Optional[str] = None
    event_stamp: Optional[str] = None
    id_user: Optional[str] = None
    flag_for_curator: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitableThingId):
            self.id = CitableThingId(self.id)

        if not isinstance(self.has_citation, list):
            self.has_citation = [self.has_citation] if self.has_citation is not None else []
        self.has_citation = [v if isinstance(v, CitationId) else CitationId(v) for v in self.has_citation]

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        if self.creation_time is not None and not isinstance(self.creation_time, str):
            self.creation_time = str(self.creation_time)

        if self.event_stamp is not None and not isinstance(self.event_stamp, str):
            self.event_stamp = str(self.event_stamp)

        if self.id_user is not None and not isinstance(self.id_user, str):
            self.id_user = str(self.id_user)

        if self.flag_for_curator is not None and not isinstance(self.flag_for_curator, str):
            self.flag_for_curator = str(self.flag_for_curator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Task(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Task"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Task"
    class_name: ClassVar[str] = "Task"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Task

    id: Union[str, TaskId] = None
    asserts: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    has_condition: Optional[Union[Union[str, ConditionId], List[Union[str, ConditionId]]]] = empty_list()
    has_contrast: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    has_external_dataset: Optional[Union[Union[str, ExternalDatasetId], List[Union[str, ExternalDatasetId]]]] = empty_list()
    has_implementation: Optional[Union[Union[str, ImplementationId], List[Union[str, ImplementationId]]]] = empty_list()
    has_indicator: Optional[Union[Union[str, IndicatorId], List[Union[str, IndicatorId]]]] = empty_list()
    id_concept_class: Optional[str] = None
    def_id: Optional[str] = None
    review_status: Optional[str] = None
    def_event_stamp: Optional[str] = None
    def_id_user: Optional[str] = None
    definition_text: Optional[str] = None
    in_battery: Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]] = empty_list()
    event_stamp: Optional[str] = None
    alias: Optional[str] = None
    kind_of: Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]] = empty_list()
    part_of: Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaskId):
            self.id = TaskId(self.id)

        if not isinstance(self.asserts, list):
            self.asserts = [self.asserts] if self.asserts is not None else []
        self.asserts = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.asserts]

        if not isinstance(self.has_condition, list):
            self.has_condition = [self.has_condition] if self.has_condition is not None else []
        self.has_condition = [v if isinstance(v, ConditionId) else ConditionId(v) for v in self.has_condition]

        if not isinstance(self.has_contrast, list):
            self.has_contrast = [self.has_contrast] if self.has_contrast is not None else []
        self.has_contrast = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.has_contrast]

        if not isinstance(self.has_external_dataset, list):
            self.has_external_dataset = [self.has_external_dataset] if self.has_external_dataset is not None else []
        self.has_external_dataset = [v if isinstance(v, ExternalDatasetId) else ExternalDatasetId(v) for v in self.has_external_dataset]

        if not isinstance(self.has_implementation, list):
            self.has_implementation = [self.has_implementation] if self.has_implementation is not None else []
        self.has_implementation = [v if isinstance(v, ImplementationId) else ImplementationId(v) for v in self.has_implementation]

        if not isinstance(self.has_indicator, list):
            self.has_indicator = [self.has_indicator] if self.has_indicator is not None else []
        self.has_indicator = [v if isinstance(v, IndicatorId) else IndicatorId(v) for v in self.has_indicator]

        if self.id_concept_class is not None and not isinstance(self.id_concept_class, str):
            self.id_concept_class = str(self.id_concept_class)

        if self.def_id is not None and not isinstance(self.def_id, str):
            self.def_id = str(self.def_id)

        if self.review_status is not None and not isinstance(self.review_status, str):
            self.review_status = str(self.review_status)

        if self.def_event_stamp is not None and not isinstance(self.def_event_stamp, str):
            self.def_event_stamp = str(self.def_event_stamp)

        if self.def_id_user is not None and not isinstance(self.def_id_user, str):
            self.def_id_user = str(self.def_id_user)

        if self.definition_text is not None and not isinstance(self.definition_text, str):
            self.definition_text = str(self.definition_text)

        if not isinstance(self.in_battery, list):
            self.in_battery = [self.in_battery] if self.in_battery is not None else []
        self.in_battery = [v if isinstance(v, BatteryId) else BatteryId(v) for v in self.in_battery]

        if self.event_stamp is not None and not isinstance(self.event_stamp, str):
            self.event_stamp = str(self.event_stamp)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if not isinstance(self.kind_of, list):
            self.kind_of = [self.kind_of] if self.kind_of is not None else []
        self.kind_of = [v if isinstance(v, TaskId) else TaskId(v) for v in self.kind_of]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, TaskId) else TaskId(v) for v in self.part_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Concept"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Concept

    id: Union[str, ConceptId] = None
    alias: Optional[str] = None
    part_of: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    kind_of: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    measured_by: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    classified_under: Optional[Union[Union[str, ConceptClassId], List[Union[str, ConceptClassId]]]] = empty_list()
    id_concept_class: Optional[str] = None
    def_id: Optional[str] = None
    def_event_stamp: Optional[str] = None
    def_id_user: Optional[str] = None
    definition_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptId):
            self.id = ConceptId(self.id)

        if self.alias is not None and not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.part_of]

        if not isinstance(self.kind_of, list):
            self.kind_of = [self.kind_of] if self.kind_of is not None else []
        self.kind_of = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.kind_of]

        if not isinstance(self.measured_by, list):
            self.measured_by = [self.measured_by] if self.measured_by is not None else []
        self.measured_by = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.measured_by]

        if not isinstance(self.classified_under, list):
            self.classified_under = [self.classified_under] if self.classified_under is not None else []
        self.classified_under = [v if isinstance(v, ConceptClassId) else ConceptClassId(v) for v in self.classified_under]

        if self.id_concept_class is not None and not isinstance(self.id_concept_class, str):
            self.id_concept_class = str(self.id_concept_class)

        if self.def_id is not None and not isinstance(self.def_id, str):
            self.def_id = str(self.def_id)

        if self.def_event_stamp is not None and not isinstance(self.def_event_stamp, str):
            self.def_event_stamp = str(self.def_event_stamp)

        if self.def_id_user is not None and not isinstance(self.def_id_user, str):
            self.def_id_user = str(self.def_id_user)

        if self.definition_text is not None and not isinstance(self.definition_text, str):
            self.definition_text = str(self.definition_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disorder(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Disorder"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Disorder"
    class_name: ClassVar[str] = "Disorder"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Disorder

    id: Union[str, DisorderId] = None
    classification: Optional[str] = None
    definition: Optional[str] = None
    is_a: Optional[Union[Union[str, DisorderId], List[Union[str, DisorderId]]]] = empty_list()
    id_protocol: Optional[str] = None
    is_a_fulltext: Optional[str] = None
    is_a_protocol: Optional[str] = None
    has_link: Optional[Union[Union[str, ExternalLinkId], List[Union[str, ExternalLinkId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisorderId):
            self.id = DisorderId(self.id)

        if self.classification is not None and not isinstance(self.classification, str):
            self.classification = str(self.classification)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.is_a, list):
            self.is_a = [self.is_a] if self.is_a is not None else []
        self.is_a = [v if isinstance(v, DisorderId) else DisorderId(v) for v in self.is_a]

        if self.id_protocol is not None and not isinstance(self.id_protocol, str):
            self.id_protocol = str(self.id_protocol)

        if self.is_a_fulltext is not None and not isinstance(self.is_a_fulltext, str):
            self.is_a_fulltext = str(self.is_a_fulltext)

        if self.is_a_protocol is not None and not isinstance(self.is_a_protocol, str):
            self.is_a_protocol = str(self.is_a_protocol)

        if not isinstance(self.is_a, list):
            self.is_a = [self.is_a] if self.is_a is not None else []
        self.is_a = [v if isinstance(v, DisorderId) else DisorderId(v) for v in self.is_a]

        if not isinstance(self.has_link, list):
            self.has_link = [self.has_link] if self.has_link is not None else []
        self.has_link = [v if isinstance(v, ExternalLinkId) else ExternalLinkId(v) for v in self.has_link]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Trait(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Trait"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Trait"
    class_name: ClassVar[str] = "Trait"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Trait

    id: Union[str, TraitId] = None
    has_citation: Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]] = empty_list()
    has_link: Optional[Union[Union[str, ExternalLinkId], List[Union[str, ExternalLinkId]]]] = empty_list()
    measured_by: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    definition: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TraitId):
            self.id = TraitId(self.id)

        if not isinstance(self.has_citation, list):
            self.has_citation = [self.has_citation] if self.has_citation is not None else []
        self.has_citation = [v if isinstance(v, CitationId) else CitationId(v) for v in self.has_citation]

        if not isinstance(self.has_link, list):
            self.has_link = [self.has_link] if self.has_link is not None else []
        self.has_link = [v if isinstance(v, ExternalLinkId) else ExternalLinkId(v) for v in self.has_link]

        if not isinstance(self.measured_by, list):
            self.measured_by = [self.measured_by] if self.measured_by is not None else []
        self.measured_by = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.measured_by]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Behavior(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Behavior"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Behavior"
    class_name: ClassVar[str] = "Behavior"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Behavior

    id: Union[str, BehaviorId] = None
    has_citation: Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]] = empty_list()
    has_link: Optional[Union[Union[str, ExternalLinkId], List[Union[str, ExternalLinkId]]]] = empty_list()
    measured_by: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    definition: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BehaviorId):
            self.id = BehaviorId(self.id)

        if not isinstance(self.has_citation, list):
            self.has_citation = [self.has_citation] if self.has_citation is not None else []
        self.has_citation = [v if isinstance(v, CitationId) else CitationId(v) for v in self.has_citation]

        if not isinstance(self.has_link, list):
            self.has_link = [self.has_link] if self.has_link is not None else []
        self.has_link = [v if isinstance(v, ExternalLinkId) else ExternalLinkId(v) for v in self.has_link]

        if not isinstance(self.measured_by, list):
            self.measured_by = [self.measured_by] if self.measured_by is not None else []
        self.measured_by = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.measured_by]

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Condition(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Condition"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Condition"
    class_name: ClassVar[str] = "Condition"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Condition

    id: Union[str, ConditionId] = None
    has_contrast: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    condition_text: Optional[str] = None
    condition_description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConditionId):
            self.id = ConditionId(self.id)

        if not isinstance(self.has_contrast, list):
            self.has_contrast = [self.has_contrast] if self.has_contrast is not None else []
        self.has_contrast = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.has_contrast]

        if self.condition_text is not None and not isinstance(self.condition_text, str):
            self.condition_text = str(self.condition_text)

        if self.condition_description is not None and not isinstance(self.condition_description, str):
            self.condition_description = str(self.condition_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contrast(CitableThing):
    """
    Represents a Task
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Contrast"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Contrast"
    class_name: ClassVar[str] = "Contrast"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Contrast

    id: Union[str, ContrastId] = None
    has_difference: Optional[Union[Union[str, DisorderId], List[Union[str, DisorderId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContrastId):
            self.id = ContrastId(self.id)

        if not isinstance(self.has_difference, list):
            self.has_difference = [self.has_difference] if self.has_difference is not None else []
        self.has_difference = [v if isinstance(v, DisorderId) else DisorderId(v) for v in self.has_difference]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Battery(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Battery"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Battery"
    class_name: ClassVar[str] = "Battery"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Battery

    id: Union[str, BatteryId] = None
    collection: Optional[str] = None
    collection_description: Optional[str] = None
    collection_alias: Optional[str] = None
    has_citation: Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]] = empty_list()
    has_indicator: Optional[Union[Union[str, IndicatorId], List[Union[str, IndicatorId]]]] = empty_list()
    in_battery: Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]] = empty_list()
    collection_date_introduced: Optional[str] = None
    collection_publisher: Optional[str] = None
    website: Optional[str] = None
    kind_of: Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]] = empty_list()
    part_of: Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BatteryId):
            self.id = BatteryId(self.id)

        if self.collection is not None and not isinstance(self.collection, str):
            self.collection = str(self.collection)

        if self.collection_description is not None and not isinstance(self.collection_description, str):
            self.collection_description = str(self.collection_description)

        if self.collection_alias is not None and not isinstance(self.collection_alias, str):
            self.collection_alias = str(self.collection_alias)

        if not isinstance(self.has_citation, list):
            self.has_citation = [self.has_citation] if self.has_citation is not None else []
        self.has_citation = [v if isinstance(v, CitationId) else CitationId(v) for v in self.has_citation]

        if not isinstance(self.has_indicator, list):
            self.has_indicator = [self.has_indicator] if self.has_indicator is not None else []
        self.has_indicator = [v if isinstance(v, IndicatorId) else IndicatorId(v) for v in self.has_indicator]

        if not isinstance(self.in_battery, list):
            self.in_battery = [self.in_battery] if self.in_battery is not None else []
        self.in_battery = [v if isinstance(v, BatteryId) else BatteryId(v) for v in self.in_battery]

        if self.collection_date_introduced is not None and not isinstance(self.collection_date_introduced, str):
            self.collection_date_introduced = str(self.collection_date_introduced)

        if self.collection_publisher is not None and not isinstance(self.collection_publisher, str):
            self.collection_publisher = str(self.collection_publisher)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        if not isinstance(self.kind_of, list):
            self.kind_of = [self.kind_of] if self.kind_of is not None else []
        self.kind_of = [v if isinstance(v, BatteryId) else BatteryId(v) for v in self.kind_of]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, BatteryId) else BatteryId(v) for v in self.part_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Theory(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Theory"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Theory"
    class_name: ClassVar[str] = "Theory"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Theory

    id: Union[str, TheoryId] = None
    collection_description: Optional[str] = None
    collection_alias: Optional[str] = None
    kind_of: Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]] = empty_list()
    part_of: Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TheoryId):
            self.id = TheoryId(self.id)

        if self.collection_description is not None and not isinstance(self.collection_description, str):
            self.collection_description = str(self.collection_description)

        if self.collection_alias is not None and not isinstance(self.collection_alias, str):
            self.collection_alias = str(self.collection_alias)

        if not isinstance(self.kind_of, list):
            self.kind_of = [self.kind_of] if self.kind_of is not None else []
        self.kind_of = [v if isinstance(v, TheoryId) else TheoryId(v) for v in self.kind_of]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, TheoryId) else TheoryId(v) for v in self.part_of]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Implementation(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Implementation"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Implementation"
    class_name: ClassVar[str] = "Implementation"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Implementation

    id: Union[str, ImplementationId] = None
    implementation_uri: Optional[str] = None
    implementation_name: Optional[str] = None
    implementation_description: Optional[str] = None
    id_task: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImplementationId):
            self.id = ImplementationId(self.id)

        if self.implementation_uri is not None and not isinstance(self.implementation_uri, str):
            self.implementation_uri = str(self.implementation_uri)

        if self.implementation_name is not None and not isinstance(self.implementation_name, str):
            self.implementation_name = str(self.implementation_name)

        if self.implementation_description is not None and not isinstance(self.implementation_description, str):
            self.implementation_description = str(self.implementation_description)

        if self.id_task is not None and not isinstance(self.id_task, str):
            self.id_task = str(self.id_task)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalDataset(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ExternalDataset"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ExternalDataset"
    class_name: ClassVar[str] = "ExternalDataset"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ExternalDataset

    id: Union[str, ExternalDatasetId] = None
    dataset_name: Optional[str] = None
    dataset_uri: Optional[str] = None
    id_term: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExternalDatasetId):
            self.id = ExternalDatasetId(self.id)

        if self.dataset_name is not None and not isinstance(self.dataset_name, str):
            self.dataset_name = str(self.dataset_name)

        if self.dataset_uri is not None and not isinstance(self.dataset_uri, str):
            self.dataset_uri = str(self.dataset_uri)

        if self.id_term is not None and not isinstance(self.id_term, str):
            self.id_term = str(self.id_term)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Indicator(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Indicator"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Indicator"
    class_name: ClassVar[str] = "Indicator"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Indicator

    id: Union[str, IndicatorId] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndicatorId):
            self.id = IndicatorId(self.id)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Citation"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Citation

    id: Union[str, CitationId] = None
    citation_url: Optional[str] = None
    citation_comment: Optional[str] = None
    citation_desc: Optional[str] = None
    citation_authors: Optional[str] = None
    citation_type: Optional[str] = None
    citation_pubname: Optional[str] = None
    citation_pubdate: Optional[str] = None
    citation_pmid: Optional[str] = None
    citation_source: Optional[str] = None
    doi: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitationId):
            self.id = CitationId(self.id)

        if self.citation_url is not None and not isinstance(self.citation_url, str):
            self.citation_url = str(self.citation_url)

        if self.citation_comment is not None and not isinstance(self.citation_comment, str):
            self.citation_comment = str(self.citation_comment)

        if self.citation_desc is not None and not isinstance(self.citation_desc, str):
            self.citation_desc = str(self.citation_desc)

        if self.citation_authors is not None and not isinstance(self.citation_authors, str):
            self.citation_authors = str(self.citation_authors)

        if self.citation_type is not None and not isinstance(self.citation_type, str):
            self.citation_type = str(self.citation_type)

        if self.citation_pubname is not None and not isinstance(self.citation_pubname, str):
            self.citation_pubname = str(self.citation_pubname)

        if self.citation_pubdate is not None and not isinstance(self.citation_pubdate, str):
            self.citation_pubdate = str(self.citation_pubdate)

        if self.citation_pmid is not None and not isinstance(self.citation_pmid, str):
            self.citation_pmid = str(self.citation_pmid)

        if self.citation_source is not None and not isinstance(self.citation_source, str):
            self.citation_source = str(self.citation_source)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assertion(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Assertion"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Assertion

    id: Union[str, AssertionId] = None
    truth_value: Optional[str] = None
    id_subject_def: Optional[str] = None
    user_id: Optional[str] = None
    confidence_level: Optional[str] = None
    predicate: Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]] = empty_list()
    subject: Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]] = empty_list()
    predicate_def: Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]] = empty_list()
    in_theory: Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]] = empty_list()
    has_citation: Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssertionId):
            self.id = AssertionId(self.id)

        if self.truth_value is not None and not isinstance(self.truth_value, str):
            self.truth_value = str(self.truth_value)

        if self.id_subject_def is not None and not isinstance(self.id_subject_def, str):
            self.id_subject_def = str(self.id_subject_def)

        if self.user_id is not None and not isinstance(self.user_id, str):
            self.user_id = str(self.user_id)

        if self.confidence_level is not None and not isinstance(self.confidence_level, str):
            self.confidence_level = str(self.confidence_level)

        if not isinstance(self.predicate, list):
            self.predicate = [self.predicate] if self.predicate is not None else []
        self.predicate = [v if isinstance(v, TaskId) else TaskId(v) for v in self.predicate]

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, ConceptId) else ConceptId(v) for v in self.subject]

        if not isinstance(self.predicate_def, list):
            self.predicate_def = [self.predicate_def] if self.predicate_def is not None else []
        self.predicate_def = [v if isinstance(v, ContrastId) else ContrastId(v) for v in self.predicate_def]

        if not isinstance(self.in_theory, list):
            self.in_theory = [self.in_theory] if self.in_theory is not None else []
        self.in_theory = [v if isinstance(v, TheoryId) else TheoryId(v) for v in self.in_theory]

        if not isinstance(self.has_citation, list):
            self.has_citation = [self.has_citation] if self.has_citation is not None else []
        self.has_citation = [v if isinstance(v, CitationId) else CitationId(v) for v in self.has_citation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class User(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["User"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:User"
    class_name: ClassVar[str] = "User"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.User

    id: Union[str, UserId] = None
    old_user_id: Optional[str] = None
    username: Optional[str] = None
    created: Optional[Union[Union[str, CitableThingId], List[Union[str, CitableThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserId):
            self.id = UserId(self.id)

        if self.old_user_id is not None and not isinstance(self.old_user_id, str):
            self.old_user_id = str(self.old_user_id)

        if self.username is not None and not isinstance(self.username, str):
            self.username = str(self.username)

        if not isinstance(self.created, list):
            self.created = [self.created] if self.created is not None else []
        self.created = [v if isinstance(v, CitableThingId) else CitableThingId(v) for v in self.created]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalLink(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ExternalLink"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ExternalLink"
    class_name: ClassVar[str] = "ExternalLink"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ExternalLink

    id: Union[str, ExternalLinkId] = None
    uri: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExternalLinkId):
            self.id = ExternalLinkId(self.id)

        if self.uri is not None and not isinstance(self.uri, str):
            self.uri = str(self.uri)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptClass(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ConceptClass"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ConceptClass"
    class_name: ClassVar[str] = "ConceptClass"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ConceptClass

    id: Union[str, ConceptClassId] = None
    display_order: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConceptClassId):
            self.id = ConceptClassId(self.id)

        if self.display_order is not None and not isinstance(self.display_order, str):
            self.display_order = str(self.display_order)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disambiguation(CitableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["Disambiguation"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:Disambiguation"
    class_name: ClassVar[str] = "Disambiguation"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.Disambiguation

    id: Union[str, DisambiguationId] = None
    disambiguates: Optional[Union[Union[str, CitableThingId], List[Union[str, CitableThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisambiguationId):
            self.id = DisambiguationId(self.id)

        if not isinstance(self.disambiguates, list):
            self.disambiguates = [self.disambiguates] if self.disambiguates is not None else []
        self.disambiguates = [v if isinstance(v, CitableThingId) else CitableThingId(v) for v in self.disambiguates]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaskCollection(YAMLRoot):
    """
    A holder for Task objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["TaskCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:TaskCollection"
    class_name: ClassVar[str] = "TaskCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.TaskCollection

    entries: Optional[Union[Dict[Union[str, TaskId], Union[dict, Task]], List[Union[dict, Task]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Task, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssertionCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["AssertionCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:AssertionCollection"
    class_name: ClassVar[str] = "AssertionCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.AssertionCollection

    entries: Optional[Union[Dict[Union[str, AssertionId], Union[dict, Assertion]], List[Union[dict, Assertion]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Assertion, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BatteryCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["BatteryCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:BatteryCollection"
    class_name: ClassVar[str] = "BatteryCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.BatteryCollection

    entries: Optional[Union[Dict[Union[str, BatteryId], Union[dict, Battery]], List[Union[dict, Battery]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Battery, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BehaviorCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["BehaviorCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:BehaviorCollection"
    class_name: ClassVar[str] = "BehaviorCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.BehaviorCollection

    entries: Optional[Union[Dict[Union[str, BehaviorId], Union[dict, Behavior]], List[Union[dict, Behavior]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Behavior, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CitationCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["CitationCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:CitationCollection"
    class_name: ClassVar[str] = "CitationCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.CitationCollection

    entries: Optional[Union[Dict[Union[str, CitationId], Union[dict, Citation]], List[Union[dict, Citation]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Citation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ConceptCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ConceptCollection"
    class_name: ClassVar[str] = "ConceptCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ConceptCollection

    entries: Optional[Union[Dict[Union[str, ConceptId], Union[dict, Concept]], List[Union[dict, Concept]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Concept, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptClassCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ConceptClassCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ConceptClassCollection"
    class_name: ClassVar[str] = "ConceptClassCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ConceptClassCollection

    entries: Optional[Union[Dict[Union[str, ConceptClassId], Union[dict, ConceptClass]], List[Union[dict, ConceptClass]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=ConceptClass, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ConditionCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ConditionCollection"
    class_name: ClassVar[str] = "ConditionCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ConditionCollection

    entries: Optional[Union[Dict[Union[str, ConditionId], Union[dict, Condition]], List[Union[dict, Condition]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Condition, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContrastCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ContrastCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ContrastCollection"
    class_name: ClassVar[str] = "ContrastCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ContrastCollection

    entries: Optional[Union[Dict[Union[str, ContrastId], Union[dict, Contrast]], List[Union[dict, Contrast]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Contrast, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DisambiguationCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["DisambiguationCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:DisambiguationCollection"
    class_name: ClassVar[str] = "DisambiguationCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.DisambiguationCollection

    entries: Optional[Union[Dict[Union[str, DisambiguationId], Union[dict, Disambiguation]], List[Union[dict, Disambiguation]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Disambiguation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DisorderCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["DisorderCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:DisorderCollection"
    class_name: ClassVar[str] = "DisorderCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.DisorderCollection

    entries: Optional[Union[Dict[Union[str, DisorderId], Union[dict, Disorder]], List[Union[dict, Disorder]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Disorder, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalDatasetCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ExternalDatasetCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ExternalDatasetCollection"
    class_name: ClassVar[str] = "ExternalDatasetCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ExternalDatasetCollection

    entries: Optional[Union[Dict[Union[str, ExternalDatasetId], Union[dict, ExternalDataset]], List[Union[dict, ExternalDataset]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=ExternalDataset, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExternalLinkCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ExternalLinkCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ExternalLinkCollection"
    class_name: ClassVar[str] = "ExternalLinkCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ExternalLinkCollection

    entries: Optional[Union[Dict[Union[str, ExternalLinkId], Union[dict, ExternalLink]], List[Union[dict, ExternalLink]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=ExternalLink, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImplementationCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["ImplementationCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:ImplementationCollection"
    class_name: ClassVar[str] = "ImplementationCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.ImplementationCollection

    entries: Optional[Union[Dict[Union[str, ImplementationId], Union[dict, Implementation]], List[Union[dict, Implementation]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Implementation, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IndicatorCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["IndicatorCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:IndicatorCollection"
    class_name: ClassVar[str] = "IndicatorCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.IndicatorCollection

    entries: Optional[Union[Dict[Union[str, IndicatorId], Union[dict, Indicator]], List[Union[dict, Indicator]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Indicator, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TheoryCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["TheoryCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:TheoryCollection"
    class_name: ClassVar[str] = "TheoryCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.TheoryCollection

    entries: Optional[Union[Dict[Union[str, TheoryId], Union[dict, Theory]], List[Union[dict, Theory]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Theory, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TraitCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["TraitCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:TraitCollection"
    class_name: ClassVar[str] = "TraitCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.TraitCollection

    entries: Optional[Union[Dict[Union[str, TraitId], Union[dict, Trait]], List[Union[dict, Trait]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=Trait, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UserCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML["UserCollection"]
    class_class_curie: ClassVar[str] = "legacy_cogat_linkml:UserCollection"
    class_name: ClassVar[str] = "UserCollection"
    class_model_uri: ClassVar[URIRef] = LEGACY_COGAT_LINKML.UserCollection

    entries: Optional[Union[Dict[Union[str, UserId], Union[dict, User]], List[Union[dict, User]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=User, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LEGACY_COGAT_LINKML.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=LEGACY_COGAT_LINKML.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=LEGACY_COGAT_LINKML.description, domain=None, range=Optional[str])

slots.alias = Slot(uri=LEGACY_COGAT_LINKML.alias, name="alias", curie=LEGACY_COGAT_LINKML.curie('alias'),
                   model_uri=LEGACY_COGAT_LINKML.alias, domain=None, range=Optional[str])

slots.asserts = Slot(uri=LEGACY_COGAT_LINKML.asserts, name="asserts", curie=LEGACY_COGAT_LINKML.curie('asserts'),
                   model_uri=LEGACY_COGAT_LINKML.asserts, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.citation_authors = Slot(uri=LEGACY_COGAT_LINKML.citation_authors, name="citation_authors", curie=LEGACY_COGAT_LINKML.curie('citation_authors'),
                   model_uri=LEGACY_COGAT_LINKML.citation_authors, domain=None, range=Optional[str])

slots.citation_comment = Slot(uri=LEGACY_COGAT_LINKML.citation_comment, name="citation_comment", curie=LEGACY_COGAT_LINKML.curie('citation_comment'),
                   model_uri=LEGACY_COGAT_LINKML.citation_comment, domain=None, range=Optional[str])

slots.citation_desc = Slot(uri=LEGACY_COGAT_LINKML.citation_desc, name="citation_desc", curie=LEGACY_COGAT_LINKML.curie('citation_desc'),
                   model_uri=LEGACY_COGAT_LINKML.citation_desc, domain=None, range=Optional[str])

slots.citation_pmid = Slot(uri=LEGACY_COGAT_LINKML.citation_pmid, name="citation_pmid", curie=LEGACY_COGAT_LINKML.curie('citation_pmid'),
                   model_uri=LEGACY_COGAT_LINKML.citation_pmid, domain=None, range=Optional[str])

slots.citation_pubdate = Slot(uri=LEGACY_COGAT_LINKML.citation_pubdate, name="citation_pubdate", curie=LEGACY_COGAT_LINKML.curie('citation_pubdate'),
                   model_uri=LEGACY_COGAT_LINKML.citation_pubdate, domain=None, range=Optional[str])

slots.citation_pubname = Slot(uri=LEGACY_COGAT_LINKML.citation_pubname, name="citation_pubname", curie=LEGACY_COGAT_LINKML.curie('citation_pubname'),
                   model_uri=LEGACY_COGAT_LINKML.citation_pubname, domain=None, range=Optional[str])

slots.citation_source = Slot(uri=LEGACY_COGAT_LINKML.citation_source, name="citation_source", curie=LEGACY_COGAT_LINKML.curie('citation_source'),
                   model_uri=LEGACY_COGAT_LINKML.citation_source, domain=None, range=Optional[str])

slots.citation_type = Slot(uri=LEGACY_COGAT_LINKML.citation_type, name="citation_type", curie=LEGACY_COGAT_LINKML.curie('citation_type'),
                   model_uri=LEGACY_COGAT_LINKML.citation_type, domain=None, range=Optional[str])

slots.citation_url = Slot(uri=LEGACY_COGAT_LINKML.citation_url, name="citation_url", curie=LEGACY_COGAT_LINKML.curie('citation_url'),
                   model_uri=LEGACY_COGAT_LINKML.citation_url, domain=None, range=Optional[str])

slots.classification = Slot(uri=LEGACY_COGAT_LINKML.classification, name="classification", curie=LEGACY_COGAT_LINKML.curie('classification'),
                   model_uri=LEGACY_COGAT_LINKML.classification, domain=None, range=Optional[str])

slots.classified_under = Slot(uri=LEGACY_COGAT_LINKML.classified_under, name="classified_under", curie=LEGACY_COGAT_LINKML.curie('classified_under'),
                   model_uri=LEGACY_COGAT_LINKML.classified_under, domain=None, range=Optional[Union[Union[str, ConceptClassId], List[Union[str, ConceptClassId]]]])

slots.collection = Slot(uri=LEGACY_COGAT_LINKML.collection, name="collection", curie=LEGACY_COGAT_LINKML.curie('collection'),
                   model_uri=LEGACY_COGAT_LINKML.collection, domain=None, range=Optional[str])

slots.collection_description = Slot(uri=LEGACY_COGAT_LINKML.collection_description, name="collection_description", curie=LEGACY_COGAT_LINKML.curie('collection_description'),
                   model_uri=LEGACY_COGAT_LINKML.collection_description, domain=None, range=Optional[str])

slots.confidence_level = Slot(uri=LEGACY_COGAT_LINKML.confidence_level, name="confidence_level", curie=LEGACY_COGAT_LINKML.curie('confidence_level'),
                   model_uri=LEGACY_COGAT_LINKML.confidence_level, domain=None, range=Optional[str])

slots.created = Slot(uri=LEGACY_COGAT_LINKML.created, name="created", curie=LEGACY_COGAT_LINKML.curie('created'),
                   model_uri=LEGACY_COGAT_LINKML.created, domain=None, range=Optional[Union[Union[str, CitableThingId], List[Union[str, CitableThingId]]]])

slots.dataset_name = Slot(uri=LEGACY_COGAT_LINKML.dataset_name, name="dataset_name", curie=LEGACY_COGAT_LINKML.curie('dataset_name'),
                   model_uri=LEGACY_COGAT_LINKML.dataset_name, domain=None, range=Optional[str])

slots.dataset_uri = Slot(uri=LEGACY_COGAT_LINKML.dataset_uri, name="dataset_uri", curie=LEGACY_COGAT_LINKML.curie('dataset_uri'),
                   model_uri=LEGACY_COGAT_LINKML.dataset_uri, domain=None, range=Optional[str])

slots.definition = Slot(uri=LEGACY_COGAT_LINKML.definition, name="definition", curie=LEGACY_COGAT_LINKML.curie('definition'),
                   model_uri=LEGACY_COGAT_LINKML.definition, domain=None, range=Optional[str])

slots.disambiguates = Slot(uri=LEGACY_COGAT_LINKML.disambiguates, name="disambiguates", curie=LEGACY_COGAT_LINKML.curie('disambiguates'),
                   model_uri=LEGACY_COGAT_LINKML.disambiguates, domain=None, range=Optional[Union[Union[str, CitableThingId], List[Union[str, CitableThingId]]]])

slots.display_order = Slot(uri=LEGACY_COGAT_LINKML.display_order, name="display_order", curie=LEGACY_COGAT_LINKML.curie('display_order'),
                   model_uri=LEGACY_COGAT_LINKML.display_order, domain=None, range=Optional[str])

slots.event_stamp = Slot(uri=LEGACY_COGAT_LINKML.event_stamp, name="event_stamp", curie=LEGACY_COGAT_LINKML.curie('event_stamp'),
                   model_uri=LEGACY_COGAT_LINKML.event_stamp, domain=None, range=Optional[str])

slots.flag_for_curator = Slot(uri=LEGACY_COGAT_LINKML.flag_for_curator, name="flag_for_curator", curie=LEGACY_COGAT_LINKML.curie('flag_for_curator'),
                   model_uri=LEGACY_COGAT_LINKML.flag_for_curator, domain=None, range=Optional[str])

slots.has_citation = Slot(uri=LEGACY_COGAT_LINKML.has_citation, name="has_citation", curie=LEGACY_COGAT_LINKML.curie('has_citation'),
                   model_uri=LEGACY_COGAT_LINKML.has_citation, domain=None, range=Optional[Union[Union[str, CitationId], List[Union[str, CitationId]]]])

slots.has_condition = Slot(uri=LEGACY_COGAT_LINKML.has_condition, name="has_condition", curie=LEGACY_COGAT_LINKML.curie('has_condition'),
                   model_uri=LEGACY_COGAT_LINKML.has_condition, domain=None, range=Optional[Union[Union[str, ConditionId], List[Union[str, ConditionId]]]])

slots.has_contrast = Slot(uri=LEGACY_COGAT_LINKML.has_contrast, name="has_contrast", curie=LEGACY_COGAT_LINKML.curie('has_contrast'),
                   model_uri=LEGACY_COGAT_LINKML.has_contrast, domain=None, range=Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]])

slots.has_difference = Slot(uri=LEGACY_COGAT_LINKML.has_difference, name="has_difference", curie=LEGACY_COGAT_LINKML.curie('has_difference'),
                   model_uri=LEGACY_COGAT_LINKML.has_difference, domain=None, range=Optional[Union[Union[str, DisorderId], List[Union[str, DisorderId]]]])

slots.has_external_dataset = Slot(uri=LEGACY_COGAT_LINKML.has_external_dataset, name="has_external_dataset", curie=LEGACY_COGAT_LINKML.curie('has_external_dataset'),
                   model_uri=LEGACY_COGAT_LINKML.has_external_dataset, domain=None, range=Optional[Union[Union[str, ExternalDatasetId], List[Union[str, ExternalDatasetId]]]])

slots.has_implementation = Slot(uri=LEGACY_COGAT_LINKML.has_implementation, name="has_implementation", curie=LEGACY_COGAT_LINKML.curie('has_implementation'),
                   model_uri=LEGACY_COGAT_LINKML.has_implementation, domain=None, range=Optional[Union[Union[str, ImplementationId], List[Union[str, ImplementationId]]]])

slots.has_indicator = Slot(uri=LEGACY_COGAT_LINKML.has_indicator, name="has_indicator", curie=LEGACY_COGAT_LINKML.curie('has_indicator'),
                   model_uri=LEGACY_COGAT_LINKML.has_indicator, domain=None, range=Optional[Union[Union[str, IndicatorId], List[Union[str, IndicatorId]]]])

slots.has_link = Slot(uri=LEGACY_COGAT_LINKML.has_link, name="has_link", curie=LEGACY_COGAT_LINKML.curie('has_link'),
                   model_uri=LEGACY_COGAT_LINKML.has_link, domain=None, range=Optional[Union[Union[str, ExternalLinkId], List[Union[str, ExternalLinkId]]]])

slots.id_protocol = Slot(uri=LEGACY_COGAT_LINKML.id_protocol, name="id_protocol", curie=LEGACY_COGAT_LINKML.curie('id_protocol'),
                   model_uri=LEGACY_COGAT_LINKML.id_protocol, domain=None, range=Optional[str])

slots.id_subject_def = Slot(uri=LEGACY_COGAT_LINKML.id_subject_def, name="id_subject_def", curie=LEGACY_COGAT_LINKML.curie('id_subject_def'),
                   model_uri=LEGACY_COGAT_LINKML.id_subject_def, domain=None, range=Optional[str])

slots.id_user = Slot(uri=LEGACY_COGAT_LINKML.id_user, name="id_user", curie=LEGACY_COGAT_LINKML.curie('id_user'),
                   model_uri=LEGACY_COGAT_LINKML.id_user, domain=None, range=Optional[str])

slots.implementation_description = Slot(uri=LEGACY_COGAT_LINKML.implementation_description, name="implementation_description", curie=LEGACY_COGAT_LINKML.curie('implementation_description'),
                   model_uri=LEGACY_COGAT_LINKML.implementation_description, domain=None, range=Optional[str])

slots.implementation_name = Slot(uri=LEGACY_COGAT_LINKML.implementation_name, name="implementation_name", curie=LEGACY_COGAT_LINKML.curie('implementation_name'),
                   model_uri=LEGACY_COGAT_LINKML.implementation_name, domain=None, range=Optional[str])

slots.implementation_uri = Slot(uri=LEGACY_COGAT_LINKML.implementation_uri, name="implementation_uri", curie=LEGACY_COGAT_LINKML.curie('implementation_uri'),
                   model_uri=LEGACY_COGAT_LINKML.implementation_uri, domain=None, range=Optional[str])

slots.in_battery = Slot(uri=LEGACY_COGAT_LINKML.in_battery, name="in_battery", curie=LEGACY_COGAT_LINKML.curie('in_battery'),
                   model_uri=LEGACY_COGAT_LINKML.in_battery, domain=None, range=Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]])

slots.in_theory = Slot(uri=LEGACY_COGAT_LINKML.in_theory, name="in_theory", curie=LEGACY_COGAT_LINKML.curie('in_theory'),
                   model_uri=LEGACY_COGAT_LINKML.in_theory, domain=None, range=Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]])

slots.is_a = Slot(uri=LEGACY_COGAT_LINKML.is_a, name="is_a", curie=LEGACY_COGAT_LINKML.curie('is_a'),
                   model_uri=LEGACY_COGAT_LINKML.is_a, domain=None, range=Optional[Union[Union[str, DisorderId], List[Union[str, DisorderId]]]])

slots.is_a_fulltext = Slot(uri=LEGACY_COGAT_LINKML.is_a_fulltext, name="is_a_fulltext", curie=LEGACY_COGAT_LINKML.curie('is_a_fulltext'),
                   model_uri=LEGACY_COGAT_LINKML.is_a_fulltext, domain=None, range=Optional[str])

slots.is_a_protocol = Slot(uri=LEGACY_COGAT_LINKML.is_a_protocol, name="is_a_protocol", curie=LEGACY_COGAT_LINKML.curie('is_a_protocol'),
                   model_uri=LEGACY_COGAT_LINKML.is_a_protocol, domain=None, range=Optional[str])

slots.kind_of = Slot(uri=LEGACY_COGAT_LINKML.kind_of, name="kind_of", curie=LEGACY_COGAT_LINKML.curie('kind_of'),
                   model_uri=LEGACY_COGAT_LINKML.kind_of, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.measured_by = Slot(uri=LEGACY_COGAT_LINKML.measured_by, name="measured_by", curie=LEGACY_COGAT_LINKML.curie('measured_by'),
                   model_uri=LEGACY_COGAT_LINKML.measured_by, domain=None, range=Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]])

slots.old_user_id = Slot(uri=LEGACY_COGAT_LINKML.old_user_id, name="old_user_id", curie=LEGACY_COGAT_LINKML.curie('old_user_id'),
                   model_uri=LEGACY_COGAT_LINKML.old_user_id, domain=None, range=Optional[str])

slots.part_of = Slot(uri=LEGACY_COGAT_LINKML.part_of, name="part_of", curie=LEGACY_COGAT_LINKML.curie('part_of'),
                   model_uri=LEGACY_COGAT_LINKML.part_of, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.predicate = Slot(uri=LEGACY_COGAT_LINKML.predicate, name="predicate", curie=LEGACY_COGAT_LINKML.curie('predicate'),
                   model_uri=LEGACY_COGAT_LINKML.predicate, domain=None, range=Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]])

slots.predicate_def = Slot(uri=LEGACY_COGAT_LINKML.predicate_def, name="predicate_def", curie=LEGACY_COGAT_LINKML.curie('predicate_def'),
                   model_uri=LEGACY_COGAT_LINKML.predicate_def, domain=None, range=Optional[Union[Union[str, ContrastId], List[Union[str, ContrastId]]]])

slots.subject = Slot(uri=LEGACY_COGAT_LINKML.subject, name="subject", curie=LEGACY_COGAT_LINKML.curie('subject'),
                   model_uri=LEGACY_COGAT_LINKML.subject, domain=None, range=Optional[Union[Union[str, ConceptId], List[Union[str, ConceptId]]]])

slots.truth_value = Slot(uri=LEGACY_COGAT_LINKML.truth_value, name="truth_value", curie=LEGACY_COGAT_LINKML.curie('truth_value'),
                   model_uri=LEGACY_COGAT_LINKML.truth_value, domain=None, range=Optional[str])

slots.type = Slot(uri=LEGACY_COGAT_LINKML.type, name="type", curie=LEGACY_COGAT_LINKML.curie('type'),
                   model_uri=LEGACY_COGAT_LINKML.type, domain=None, range=Optional[str])

slots.uri = Slot(uri=LEGACY_COGAT_LINKML.uri, name="uri", curie=LEGACY_COGAT_LINKML.curie('uri'),
                   model_uri=LEGACY_COGAT_LINKML.uri, domain=None, range=Optional[str])

slots.user_id = Slot(uri=LEGACY_COGAT_LINKML.user_id, name="user_id", curie=LEGACY_COGAT_LINKML.curie('user_id'),
                   model_uri=LEGACY_COGAT_LINKML.user_id, domain=None, range=Optional[str])

slots.username = Slot(uri=LEGACY_COGAT_LINKML.username, name="username", curie=LEGACY_COGAT_LINKML.curie('username'),
                   model_uri=LEGACY_COGAT_LINKML.username, domain=None, range=Optional[str])

slots.last_updated = Slot(uri=LEGACY_COGAT_LINKML.last_updated, name="last_updated", curie=LEGACY_COGAT_LINKML.curie('last_updated'),
                   model_uri=LEGACY_COGAT_LINKML.last_updated, domain=None, range=Optional[str])

slots.creation_time = Slot(uri=LEGACY_COGAT_LINKML.creation_time, name="creation_time", curie=LEGACY_COGAT_LINKML.curie('creation_time'),
                   model_uri=LEGACY_COGAT_LINKML.creation_time, domain=None, range=Optional[str])

slots.collection_alias = Slot(uri=LEGACY_COGAT_LINKML.collection_alias, name="collection_alias", curie=LEGACY_COGAT_LINKML.curie('collection_alias'),
                   model_uri=LEGACY_COGAT_LINKML.collection_alias, domain=None, range=Optional[str])

slots.collection_date_introduced = Slot(uri=LEGACY_COGAT_LINKML.collection_date_introduced, name="collection_date_introduced", curie=LEGACY_COGAT_LINKML.curie('collection_date_introduced'),
                   model_uri=LEGACY_COGAT_LINKML.collection_date_introduced, domain=None, range=Optional[str])

slots.collection_publisher = Slot(uri=LEGACY_COGAT_LINKML.collection_publisher, name="collection_publisher", curie=LEGACY_COGAT_LINKML.curie('collection_publisher'),
                   model_uri=LEGACY_COGAT_LINKML.collection_publisher, domain=None, range=Optional[str])

slots.condition_description = Slot(uri=LEGACY_COGAT_LINKML.condition_description, name="condition_description", curie=LEGACY_COGAT_LINKML.curie('condition_description'),
                   model_uri=LEGACY_COGAT_LINKML.condition_description, domain=None, range=Optional[str])

slots.condition_text = Slot(uri=LEGACY_COGAT_LINKML.condition_text, name="condition_text", curie=LEGACY_COGAT_LINKML.curie('condition_text'),
                   model_uri=LEGACY_COGAT_LINKML.condition_text, domain=None, range=Optional[str])

slots.def_event_stamp = Slot(uri=LEGACY_COGAT_LINKML.def_event_stamp, name="def_event_stamp", curie=LEGACY_COGAT_LINKML.curie('def_event_stamp'),
                   model_uri=LEGACY_COGAT_LINKML.def_event_stamp, domain=None, range=Optional[str])

slots.def_id = Slot(uri=LEGACY_COGAT_LINKML.def_id, name="def_id", curie=LEGACY_COGAT_LINKML.curie('def_id'),
                   model_uri=LEGACY_COGAT_LINKML.def_id, domain=None, range=Optional[str])

slots.def_id_user = Slot(uri=LEGACY_COGAT_LINKML.def_id_user, name="def_id_user", curie=LEGACY_COGAT_LINKML.curie('def_id_user'),
                   model_uri=LEGACY_COGAT_LINKML.def_id_user, domain=None, range=Optional[str])

slots.definition_text = Slot(uri=LEGACY_COGAT_LINKML.definition_text, name="definition_text", curie=LEGACY_COGAT_LINKML.curie('definition_text'),
                   model_uri=LEGACY_COGAT_LINKML.definition_text, domain=None, range=Optional[str])

slots.doi = Slot(uri=LEGACY_COGAT_LINKML.doi, name="doi", curie=LEGACY_COGAT_LINKML.curie('doi'),
                   model_uri=LEGACY_COGAT_LINKML.doi, domain=None, range=Optional[str])

slots.id_concept_class = Slot(uri=LEGACY_COGAT_LINKML.id_concept_class, name="id_concept_class", curie=LEGACY_COGAT_LINKML.curie('id_concept_class'),
                   model_uri=LEGACY_COGAT_LINKML.id_concept_class, domain=None, range=Optional[str])

slots.id_task = Slot(uri=LEGACY_COGAT_LINKML.id_task, name="id_task", curie=LEGACY_COGAT_LINKML.curie('id_task'),
                   model_uri=LEGACY_COGAT_LINKML.id_task, domain=None, range=Optional[str])

slots.id_term = Slot(uri=LEGACY_COGAT_LINKML.id_term, name="id_term", curie=LEGACY_COGAT_LINKML.curie('id_term'),
                   model_uri=LEGACY_COGAT_LINKML.id_term, domain=None, range=Optional[str])

slots.review_status = Slot(uri=LEGACY_COGAT_LINKML.review_status, name="review_status", curie=LEGACY_COGAT_LINKML.curie('review_status'),
                   model_uri=LEGACY_COGAT_LINKML.review_status, domain=None, range=Optional[str])

slots.website = Slot(uri=LEGACY_COGAT_LINKML.website, name="website", curie=LEGACY_COGAT_LINKML.curie('website'),
                   model_uri=LEGACY_COGAT_LINKML.website, domain=None, range=Optional[str])

slots.task__kind_of = Slot(uri=LEGACY_COGAT_LINKML.kind_of, name="task__kind_of", curie=LEGACY_COGAT_LINKML.curie('kind_of'),
                   model_uri=LEGACY_COGAT_LINKML.task__kind_of, domain=None, range=Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]])

slots.task__part_of = Slot(uri=LEGACY_COGAT_LINKML.part_of, name="task__part_of", curie=LEGACY_COGAT_LINKML.curie('part_of'),
                   model_uri=LEGACY_COGAT_LINKML.task__part_of, domain=None, range=Optional[Union[Union[str, TaskId], List[Union[str, TaskId]]]])

slots.battery__kind_of = Slot(uri=LEGACY_COGAT_LINKML.kind_of, name="battery__kind_of", curie=LEGACY_COGAT_LINKML.curie('kind_of'),
                   model_uri=LEGACY_COGAT_LINKML.battery__kind_of, domain=None, range=Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]])

slots.battery__part_of = Slot(uri=LEGACY_COGAT_LINKML.part_of, name="battery__part_of", curie=LEGACY_COGAT_LINKML.curie('part_of'),
                   model_uri=LEGACY_COGAT_LINKML.battery__part_of, domain=None, range=Optional[Union[Union[str, BatteryId], List[Union[str, BatteryId]]]])

slots.theory__kind_of = Slot(uri=LEGACY_COGAT_LINKML.kind_of, name="theory__kind_of", curie=LEGACY_COGAT_LINKML.curie('kind_of'),
                   model_uri=LEGACY_COGAT_LINKML.theory__kind_of, domain=None, range=Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]])

slots.theory__part_of = Slot(uri=LEGACY_COGAT_LINKML.part_of, name="theory__part_of", curie=LEGACY_COGAT_LINKML.curie('part_of'),
                   model_uri=LEGACY_COGAT_LINKML.theory__part_of, domain=None, range=Optional[Union[Union[str, TheoryId], List[Union[str, TheoryId]]]])

slots.taskCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="taskCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.taskCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, TaskId], Union[dict, Task]], List[Union[dict, Task]]]])

slots.assertionCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="assertionCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.assertionCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, AssertionId], Union[dict, Assertion]], List[Union[dict, Assertion]]]])

slots.batteryCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="batteryCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.batteryCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, BatteryId], Union[dict, Battery]], List[Union[dict, Battery]]]])

slots.behaviorCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="behaviorCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.behaviorCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, BehaviorId], Union[dict, Behavior]], List[Union[dict, Behavior]]]])

slots.citationCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="citationCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.citationCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, CitationId], Union[dict, Citation]], List[Union[dict, Citation]]]])

slots.conceptCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="conceptCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.conceptCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ConceptId], Union[dict, Concept]], List[Union[dict, Concept]]]])

slots.conceptClassCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="conceptClassCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.conceptClassCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ConceptClassId], Union[dict, ConceptClass]], List[Union[dict, ConceptClass]]]])

slots.conditionCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="conditionCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.conditionCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ConditionId], Union[dict, Condition]], List[Union[dict, Condition]]]])

slots.contrastCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="contrastCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.contrastCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ContrastId], Union[dict, Contrast]], List[Union[dict, Contrast]]]])

slots.disambiguationCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="disambiguationCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.disambiguationCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, DisambiguationId], Union[dict, Disambiguation]], List[Union[dict, Disambiguation]]]])

slots.disorderCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="disorderCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.disorderCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, DisorderId], Union[dict, Disorder]], List[Union[dict, Disorder]]]])

slots.externalDatasetCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="externalDatasetCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.externalDatasetCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ExternalDatasetId], Union[dict, ExternalDataset]], List[Union[dict, ExternalDataset]]]])

slots.externalLinkCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="externalLinkCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.externalLinkCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ExternalLinkId], Union[dict, ExternalLink]], List[Union[dict, ExternalLink]]]])

slots.implementationCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="implementationCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.implementationCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ImplementationId], Union[dict, Implementation]], List[Union[dict, Implementation]]]])

slots.indicatorCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="indicatorCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.indicatorCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, IndicatorId], Union[dict, Indicator]], List[Union[dict, Indicator]]]])

slots.theoryCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="theoryCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.theoryCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, TheoryId], Union[dict, Theory]], List[Union[dict, Theory]]]])

slots.traitCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="traitCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.traitCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, TraitId], Union[dict, Trait]], List[Union[dict, Trait]]]])

slots.userCollection__entries = Slot(uri=LEGACY_COGAT_LINKML.entries, name="userCollection__entries", curie=LEGACY_COGAT_LINKML.curie('entries'),
                   model_uri=LEGACY_COGAT_LINKML.userCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, UserId], Union[dict, User]], List[Union[dict, User]]]])