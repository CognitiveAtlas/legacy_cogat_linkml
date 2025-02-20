-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "CitableThing" Description: "A generic grouping for any identifiable entity"
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
-- # Class: "Task" Description: "Represents a Task"
--     * Slot: id_concept_class Description: 
--     * Slot: def_id Description: 
--     * Slot: review_status Description: 
--     * Slot: def_event_stamp Description: 
--     * Slot: def_id_user Description: 
--     * Slot: definition_text Description: 
--     * Slot: event_stamp Description: 
--     * Slot: alias Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: TaskCollection_id Description: Autocreated FK slot
-- # Class: "Concept" Description: "Represents a Task"
--     * Slot: alias Description: 
--     * Slot: id_concept_class Description: 
--     * Slot: def_id Description: 
--     * Slot: def_event_stamp Description: 
--     * Slot: def_id_user Description: 
--     * Slot: definition_text Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ConceptCollection_id Description: Autocreated FK slot
-- # Class: "Disorder" Description: "Represents a Task"
--     * Slot: classification Description: 
--     * Slot: definition Description: 
--     * Slot: id_protocol Description: 
--     * Slot: is_a_fulltext Description: 
--     * Slot: is_a_protocol Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: DisorderCollection_id Description: Autocreated FK slot
-- # Class: "Trait" Description: "Represents a Task"
--     * Slot: definition Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: TraitCollection_id Description: Autocreated FK slot
-- # Class: "Behavior" Description: "Represents a Task"
--     * Slot: definition Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: BehaviorCollection_id Description: Autocreated FK slot
-- # Class: "Condition" Description: "Represents a Task"
--     * Slot: condition_text Description: 
--     * Slot: condition_description Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ConditionCollection_id Description: Autocreated FK slot
-- # Class: "Contrast" Description: "Represents a Task"
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ContrastCollection_id Description: Autocreated FK slot
-- # Class: "Battery" Description: ""
--     * Slot: collection Description: 
--     * Slot: collection_description Description: 
--     * Slot: collection_alias Description: 
--     * Slot: collection_date_introduced Description: 
--     * Slot: collection_publisher Description: 
--     * Slot: website Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: BatteryCollection_id Description: Autocreated FK slot
-- # Class: "Theory" Description: ""
--     * Slot: collection_description Description: 
--     * Slot: collection_alias Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: TheoryCollection_id Description: Autocreated FK slot
-- # Class: "Implementation" Description: ""
--     * Slot: implementation_uri Description: 
--     * Slot: implementation_name Description: 
--     * Slot: implementation_description Description: 
--     * Slot: id_task Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ImplementationCollection_id Description: Autocreated FK slot
-- # Class: "ExternalDataset" Description: ""
--     * Slot: dataset_name Description: 
--     * Slot: dataset_uri Description: 
--     * Slot: id_term Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ExternalDatasetCollection_id Description: Autocreated FK slot
-- # Class: "Indicator" Description: ""
--     * Slot: type Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: IndicatorCollection_id Description: Autocreated FK slot
-- # Class: "Citation" Description: ""
--     * Slot: citation_url Description: 
--     * Slot: citation_comment Description: 
--     * Slot: citation_desc Description: 
--     * Slot: citation_authors Description: 
--     * Slot: citation_type Description: 
--     * Slot: citation_pubname Description: 
--     * Slot: citation_pubdate Description: 
--     * Slot: citation_pmid Description: 
--     * Slot: citation_source Description: 
--     * Slot: doi Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: CitationCollection_id Description: Autocreated FK slot
-- # Class: "Assertion" Description: ""
--     * Slot: truth_value Description: 
--     * Slot: id_subject_def Description: 
--     * Slot: user_id Description: 
--     * Slot: confidence_level Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: AssertionCollection_id Description: Autocreated FK slot
-- # Class: "User" Description: ""
--     * Slot: old_user_id Description: The original PHP based site had user ids of the pattern "usr_[[:alnum:]]*". If an id of this kind existed for the user it is stored here.
--     * Slot: username Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: UserCollection_id Description: Autocreated FK slot
-- # Class: "ExternalLink" Description: ""
--     * Slot: uri Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ExternalLinkCollection_id Description: Autocreated FK slot
-- # Class: "ConceptClass" Description: ""
--     * Slot: display_order Description: 
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: ConceptClassCollection_id Description: Autocreated FK slot
-- # Class: "Disambiguation" Description: ""
--     * Slot: last_updated Description: 
--     * Slot: creation_time Description: 
--     * Slot: event_stamp Description: 
--     * Slot: id_user Description: 
--     * Slot: flag_for_curator Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: description Description: A human-readable description for a thing
--     * Slot: DisambiguationCollection_id Description: Autocreated FK slot
-- # Class: "TaskCollection" Description: "A holder for Task objects"
--     * Slot: id Description: 
-- # Class: "AssertionCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "BatteryCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "BehaviorCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "CitationCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ConceptCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ConceptClassCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ConditionCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ContrastCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "DisambiguationCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "DisorderCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ExternalDatasetCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ExternalLinkCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "ImplementationCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "IndicatorCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "TheoryCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "TraitCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "UserCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "CitableThing_has_citation" Description: ""
--     * Slot: CitableThing_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Task_asserts" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: asserts_id Description: 
-- # Class: "Task_has_condition" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_condition_id Description: 
-- # Class: "Task_has_contrast" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_contrast_id Description: 
-- # Class: "Task_has_external_dataset" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_external_dataset_id Description: 
-- # Class: "Task_has_implementation" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_implementation_id Description: 
-- # Class: "Task_has_indicator" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_indicator_id Description: 
-- # Class: "Task_in_battery" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: in_battery_id Description: 
-- # Class: "Task_kind_of" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: kind_of_id Description: 
-- # Class: "Task_part_of" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: part_of_id Description: 
-- # Class: "Task_has_citation" Description: ""
--     * Slot: Task_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Concept_part_of" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: part_of_id Description: 
-- # Class: "Concept_kind_of" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: kind_of_id Description: 
-- # Class: "Concept_measured_by" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: measured_by_id Description: 
-- # Class: "Concept_classified_under" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: classified_under_id Description: 
-- # Class: "Concept_has_citation" Description: ""
--     * Slot: Concept_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Disorder_is_a" Description: ""
--     * Slot: Disorder_id Description: Autocreated FK slot
--     * Slot: is_a_id Description: 
-- # Class: "Disorder_has_link" Description: ""
--     * Slot: Disorder_id Description: Autocreated FK slot
--     * Slot: has_link_id Description: 
-- # Class: "Disorder_has_citation" Description: ""
--     * Slot: Disorder_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Trait_has_citation" Description: ""
--     * Slot: Trait_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Trait_has_link" Description: ""
--     * Slot: Trait_id Description: Autocreated FK slot
--     * Slot: has_link_id Description: 
-- # Class: "Trait_measured_by" Description: ""
--     * Slot: Trait_id Description: Autocreated FK slot
--     * Slot: measured_by_id Description: 
-- # Class: "Behavior_has_citation" Description: ""
--     * Slot: Behavior_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Behavior_has_link" Description: ""
--     * Slot: Behavior_id Description: Autocreated FK slot
--     * Slot: has_link_id Description: 
-- # Class: "Behavior_measured_by" Description: ""
--     * Slot: Behavior_id Description: Autocreated FK slot
--     * Slot: measured_by_id Description: 
-- # Class: "Condition_has_contrast" Description: ""
--     * Slot: Condition_id Description: Autocreated FK slot
--     * Slot: has_contrast_id Description: 
-- # Class: "Condition_has_citation" Description: ""
--     * Slot: Condition_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Contrast_has_difference" Description: ""
--     * Slot: Contrast_id Description: Autocreated FK slot
--     * Slot: has_difference_id Description: 
-- # Class: "Contrast_has_citation" Description: ""
--     * Slot: Contrast_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Battery_has_citation" Description: ""
--     * Slot: Battery_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Battery_has_indicator" Description: ""
--     * Slot: Battery_id Description: Autocreated FK slot
--     * Slot: has_indicator_id Description: 
-- # Class: "Battery_in_battery" Description: ""
--     * Slot: Battery_id Description: Autocreated FK slot
--     * Slot: in_battery_id Description: 
-- # Class: "Battery_kind_of" Description: ""
--     * Slot: Battery_id Description: Autocreated FK slot
--     * Slot: kind_of_id Description: 
-- # Class: "Battery_part_of" Description: ""
--     * Slot: Battery_id Description: Autocreated FK slot
--     * Slot: part_of_id Description: 
-- # Class: "Theory_kind_of" Description: ""
--     * Slot: Theory_id Description: Autocreated FK slot
--     * Slot: kind_of_id Description: 
-- # Class: "Theory_part_of" Description: ""
--     * Slot: Theory_id Description: Autocreated FK slot
--     * Slot: part_of_id Description: 
-- # Class: "Theory_has_citation" Description: ""
--     * Slot: Theory_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Implementation_has_citation" Description: ""
--     * Slot: Implementation_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "ExternalDataset_has_citation" Description: ""
--     * Slot: ExternalDataset_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Indicator_has_citation" Description: ""
--     * Slot: Indicator_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Citation_has_citation" Description: ""
--     * Slot: Citation_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Assertion_predicate" Description: ""
--     * Slot: Assertion_id Description: Autocreated FK slot
--     * Slot: predicate_id Description: 
-- # Class: "Assertion_subject" Description: ""
--     * Slot: Assertion_id Description: Autocreated FK slot
--     * Slot: subject_id Description: 
-- # Class: "Assertion_predicate_def" Description: ""
--     * Slot: Assertion_id Description: Autocreated FK slot
--     * Slot: predicate_def_id Description: 
-- # Class: "Assertion_in_theory" Description: ""
--     * Slot: Assertion_id Description: Autocreated FK slot
--     * Slot: in_theory_id Description: 
-- # Class: "Assertion_has_citation" Description: ""
--     * Slot: Assertion_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "User_created" Description: ""
--     * Slot: User_id Description: Autocreated FK slot
--     * Slot: created_id Description: 
-- # Class: "User_has_citation" Description: ""
--     * Slot: User_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "ExternalLink_has_citation" Description: ""
--     * Slot: ExternalLink_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "ConceptClass_has_citation" Description: ""
--     * Slot: ConceptClass_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 
-- # Class: "Disambiguation_disambiguates" Description: ""
--     * Slot: Disambiguation_id Description: Autocreated FK slot
--     * Slot: disambiguates_id Description: Could apply to Concepts, Tasks, Traits...
-- # Class: "Disambiguation_has_citation" Description: ""
--     * Slot: Disambiguation_id Description: Autocreated FK slot
--     * Slot: has_citation_id Description: 

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CitableThing" (
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "TaskCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AssertionCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "BatteryCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "BehaviorCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CitationCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ConceptCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ConceptClassCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ConditionCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ContrastCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DisambiguationCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "DisorderCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ExternalDatasetCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ExternalLinkCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ImplementationCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "IndicatorCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "TheoryCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "TraitCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "UserCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Task" (
	id_concept_class TEXT, 
	def_id TEXT, 
	review_status TEXT, 
	def_event_stamp TEXT, 
	def_id_user TEXT, 
	definition_text TEXT, 
	event_stamp TEXT, 
	alias TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TaskCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TaskCollection_id") REFERENCES "TaskCollection" (id)
);
CREATE TABLE "Concept" (
	alias TEXT, 
	id_concept_class TEXT, 
	def_id TEXT, 
	def_event_stamp TEXT, 
	def_id_user TEXT, 
	definition_text TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ConceptCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ConceptCollection_id") REFERENCES "ConceptCollection" (id)
);
CREATE TABLE "Disorder" (
	classification TEXT, 
	definition TEXT, 
	id_protocol TEXT, 
	is_a_fulltext TEXT, 
	is_a_protocol TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"DisorderCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DisorderCollection_id") REFERENCES "DisorderCollection" (id)
);
CREATE TABLE "Trait" (
	definition TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TraitCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TraitCollection_id") REFERENCES "TraitCollection" (id)
);
CREATE TABLE "Behavior" (
	definition TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"BehaviorCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BehaviorCollection_id") REFERENCES "BehaviorCollection" (id)
);
CREATE TABLE "Condition" (
	condition_text TEXT, 
	condition_description TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ConditionCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ConditionCollection_id") REFERENCES "ConditionCollection" (id)
);
CREATE TABLE "Contrast" (
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ContrastCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ContrastCollection_id") REFERENCES "ContrastCollection" (id)
);
CREATE TABLE "Battery" (
	collection TEXT, 
	collection_description TEXT, 
	collection_alias TEXT, 
	collection_date_introduced TEXT, 
	collection_publisher TEXT, 
	website TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"BatteryCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BatteryCollection_id") REFERENCES "BatteryCollection" (id)
);
CREATE TABLE "Theory" (
	collection_description TEXT, 
	collection_alias TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TheoryCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TheoryCollection_id") REFERENCES "TheoryCollection" (id)
);
CREATE TABLE "Implementation" (
	implementation_uri TEXT, 
	implementation_name TEXT, 
	implementation_description TEXT, 
	id_task TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ImplementationCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ImplementationCollection_id") REFERENCES "ImplementationCollection" (id)
);
CREATE TABLE "ExternalDataset" (
	dataset_name TEXT, 
	dataset_uri TEXT, 
	id_term TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ExternalDatasetCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ExternalDatasetCollection_id") REFERENCES "ExternalDatasetCollection" (id)
);
CREATE TABLE "Indicator" (
	type TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"IndicatorCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("IndicatorCollection_id") REFERENCES "IndicatorCollection" (id)
);
CREATE TABLE "Citation" (
	citation_url TEXT, 
	citation_comment TEXT, 
	citation_desc TEXT, 
	citation_authors TEXT, 
	citation_type TEXT, 
	citation_pubname TEXT, 
	citation_pubdate TEXT, 
	citation_pmid TEXT, 
	citation_source TEXT, 
	doi TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"CitationCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("CitationCollection_id") REFERENCES "CitationCollection" (id)
);
CREATE TABLE "Assertion" (
	truth_value TEXT, 
	id_subject_def TEXT, 
	user_id TEXT, 
	confidence_level TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"AssertionCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AssertionCollection_id") REFERENCES "AssertionCollection" (id)
);
CREATE TABLE "User" (
	old_user_id TEXT, 
	username TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"UserCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("UserCollection_id") REFERENCES "UserCollection" (id)
);
CREATE TABLE "ExternalLink" (
	uri TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ExternalLinkCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ExternalLinkCollection_id") REFERENCES "ExternalLinkCollection" (id)
);
CREATE TABLE "ConceptClass" (
	display_order TEXT, 
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"ConceptClassCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ConceptClassCollection_id") REFERENCES "ConceptClassCollection" (id)
);
CREATE TABLE "Disambiguation" (
	last_updated TEXT, 
	creation_time TEXT, 
	event_stamp TEXT, 
	id_user TEXT, 
	flag_for_curator TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"DisambiguationCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DisambiguationCollection_id") REFERENCES "DisambiguationCollection" (id)
);
CREATE TABLE "CitableThing_has_citation" (
	"CitableThing_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("CitableThing_id", has_citation_id), 
	FOREIGN KEY("CitableThing_id") REFERENCES "CitableThing" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Task_asserts" (
	"Task_id" TEXT, 
	asserts_id TEXT, 
	PRIMARY KEY ("Task_id", asserts_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(asserts_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Task_has_condition" (
	"Task_id" TEXT, 
	has_condition_id TEXT, 
	PRIMARY KEY ("Task_id", has_condition_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_condition_id) REFERENCES "Condition" (id)
);
CREATE TABLE "Task_has_contrast" (
	"Task_id" TEXT, 
	has_contrast_id TEXT, 
	PRIMARY KEY ("Task_id", has_contrast_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_contrast_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Task_has_external_dataset" (
	"Task_id" TEXT, 
	has_external_dataset_id TEXT, 
	PRIMARY KEY ("Task_id", has_external_dataset_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_external_dataset_id) REFERENCES "ExternalDataset" (id)
);
CREATE TABLE "Task_has_implementation" (
	"Task_id" TEXT, 
	has_implementation_id TEXT, 
	PRIMARY KEY ("Task_id", has_implementation_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_implementation_id) REFERENCES "Implementation" (id)
);
CREATE TABLE "Task_has_indicator" (
	"Task_id" TEXT, 
	has_indicator_id TEXT, 
	PRIMARY KEY ("Task_id", has_indicator_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_indicator_id) REFERENCES "Indicator" (id)
);
CREATE TABLE "Task_in_battery" (
	"Task_id" TEXT, 
	in_battery_id TEXT, 
	PRIMARY KEY ("Task_id", in_battery_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(in_battery_id) REFERENCES "Battery" (id)
);
CREATE TABLE "Task_kind_of" (
	"Task_id" TEXT, 
	kind_of_id TEXT, 
	PRIMARY KEY ("Task_id", kind_of_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(kind_of_id) REFERENCES "Task" (id)
);
CREATE TABLE "Task_part_of" (
	"Task_id" TEXT, 
	part_of_id TEXT, 
	PRIMARY KEY ("Task_id", part_of_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(part_of_id) REFERENCES "Task" (id)
);
CREATE TABLE "Task_has_citation" (
	"Task_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Task_id", has_citation_id), 
	FOREIGN KEY("Task_id") REFERENCES "Task" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Concept_part_of" (
	"Concept_id" TEXT, 
	part_of_id TEXT, 
	PRIMARY KEY ("Concept_id", part_of_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(part_of_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Concept_kind_of" (
	"Concept_id" TEXT, 
	kind_of_id TEXT, 
	PRIMARY KEY ("Concept_id", kind_of_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(kind_of_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Concept_measured_by" (
	"Concept_id" TEXT, 
	measured_by_id TEXT, 
	PRIMARY KEY ("Concept_id", measured_by_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(measured_by_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Concept_classified_under" (
	"Concept_id" TEXT, 
	classified_under_id TEXT, 
	PRIMARY KEY ("Concept_id", classified_under_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(classified_under_id) REFERENCES "ConceptClass" (id)
);
CREATE TABLE "Concept_has_citation" (
	"Concept_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Concept_id", has_citation_id), 
	FOREIGN KEY("Concept_id") REFERENCES "Concept" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Disorder_is_a" (
	"Disorder_id" TEXT, 
	is_a_id TEXT, 
	PRIMARY KEY ("Disorder_id", is_a_id), 
	FOREIGN KEY("Disorder_id") REFERENCES "Disorder" (id), 
	FOREIGN KEY(is_a_id) REFERENCES "Disorder" (id)
);
CREATE TABLE "Disorder_has_link" (
	"Disorder_id" TEXT, 
	has_link_id TEXT, 
	PRIMARY KEY ("Disorder_id", has_link_id), 
	FOREIGN KEY("Disorder_id") REFERENCES "Disorder" (id), 
	FOREIGN KEY(has_link_id) REFERENCES "ExternalLink" (id)
);
CREATE TABLE "Disorder_has_citation" (
	"Disorder_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Disorder_id", has_citation_id), 
	FOREIGN KEY("Disorder_id") REFERENCES "Disorder" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Trait_has_citation" (
	"Trait_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Trait_id", has_citation_id), 
	FOREIGN KEY("Trait_id") REFERENCES "Trait" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Trait_has_link" (
	"Trait_id" TEXT, 
	has_link_id TEXT, 
	PRIMARY KEY ("Trait_id", has_link_id), 
	FOREIGN KEY("Trait_id") REFERENCES "Trait" (id), 
	FOREIGN KEY(has_link_id) REFERENCES "ExternalLink" (id)
);
CREATE TABLE "Trait_measured_by" (
	"Trait_id" TEXT, 
	measured_by_id TEXT, 
	PRIMARY KEY ("Trait_id", measured_by_id), 
	FOREIGN KEY("Trait_id") REFERENCES "Trait" (id), 
	FOREIGN KEY(measured_by_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Behavior_has_citation" (
	"Behavior_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Behavior_id", has_citation_id), 
	FOREIGN KEY("Behavior_id") REFERENCES "Behavior" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Behavior_has_link" (
	"Behavior_id" TEXT, 
	has_link_id TEXT, 
	PRIMARY KEY ("Behavior_id", has_link_id), 
	FOREIGN KEY("Behavior_id") REFERENCES "Behavior" (id), 
	FOREIGN KEY(has_link_id) REFERENCES "ExternalLink" (id)
);
CREATE TABLE "Behavior_measured_by" (
	"Behavior_id" TEXT, 
	measured_by_id TEXT, 
	PRIMARY KEY ("Behavior_id", measured_by_id), 
	FOREIGN KEY("Behavior_id") REFERENCES "Behavior" (id), 
	FOREIGN KEY(measured_by_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Condition_has_contrast" (
	"Condition_id" TEXT, 
	has_contrast_id TEXT, 
	PRIMARY KEY ("Condition_id", has_contrast_id), 
	FOREIGN KEY("Condition_id") REFERENCES "Condition" (id), 
	FOREIGN KEY(has_contrast_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Condition_has_citation" (
	"Condition_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Condition_id", has_citation_id), 
	FOREIGN KEY("Condition_id") REFERENCES "Condition" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Contrast_has_difference" (
	"Contrast_id" TEXT, 
	has_difference_id TEXT, 
	PRIMARY KEY ("Contrast_id", has_difference_id), 
	FOREIGN KEY("Contrast_id") REFERENCES "Contrast" (id), 
	FOREIGN KEY(has_difference_id) REFERENCES "Disorder" (id)
);
CREATE TABLE "Contrast_has_citation" (
	"Contrast_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Contrast_id", has_citation_id), 
	FOREIGN KEY("Contrast_id") REFERENCES "Contrast" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Battery_has_citation" (
	"Battery_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Battery_id", has_citation_id), 
	FOREIGN KEY("Battery_id") REFERENCES "Battery" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Battery_has_indicator" (
	"Battery_id" TEXT, 
	has_indicator_id TEXT, 
	PRIMARY KEY ("Battery_id", has_indicator_id), 
	FOREIGN KEY("Battery_id") REFERENCES "Battery" (id), 
	FOREIGN KEY(has_indicator_id) REFERENCES "Indicator" (id)
);
CREATE TABLE "Battery_in_battery" (
	"Battery_id" TEXT, 
	in_battery_id TEXT, 
	PRIMARY KEY ("Battery_id", in_battery_id), 
	FOREIGN KEY("Battery_id") REFERENCES "Battery" (id), 
	FOREIGN KEY(in_battery_id) REFERENCES "Battery" (id)
);
CREATE TABLE "Battery_kind_of" (
	"Battery_id" TEXT, 
	kind_of_id TEXT, 
	PRIMARY KEY ("Battery_id", kind_of_id), 
	FOREIGN KEY("Battery_id") REFERENCES "Battery" (id), 
	FOREIGN KEY(kind_of_id) REFERENCES "Battery" (id)
);
CREATE TABLE "Battery_part_of" (
	"Battery_id" TEXT, 
	part_of_id TEXT, 
	PRIMARY KEY ("Battery_id", part_of_id), 
	FOREIGN KEY("Battery_id") REFERENCES "Battery" (id), 
	FOREIGN KEY(part_of_id) REFERENCES "Battery" (id)
);
CREATE TABLE "Theory_kind_of" (
	"Theory_id" TEXT, 
	kind_of_id TEXT, 
	PRIMARY KEY ("Theory_id", kind_of_id), 
	FOREIGN KEY("Theory_id") REFERENCES "Theory" (id), 
	FOREIGN KEY(kind_of_id) REFERENCES "Theory" (id)
);
CREATE TABLE "Theory_part_of" (
	"Theory_id" TEXT, 
	part_of_id TEXT, 
	PRIMARY KEY ("Theory_id", part_of_id), 
	FOREIGN KEY("Theory_id") REFERENCES "Theory" (id), 
	FOREIGN KEY(part_of_id) REFERENCES "Theory" (id)
);
CREATE TABLE "Theory_has_citation" (
	"Theory_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Theory_id", has_citation_id), 
	FOREIGN KEY("Theory_id") REFERENCES "Theory" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Implementation_has_citation" (
	"Implementation_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Implementation_id", has_citation_id), 
	FOREIGN KEY("Implementation_id") REFERENCES "Implementation" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "ExternalDataset_has_citation" (
	"ExternalDataset_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("ExternalDataset_id", has_citation_id), 
	FOREIGN KEY("ExternalDataset_id") REFERENCES "ExternalDataset" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Indicator_has_citation" (
	"Indicator_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Indicator_id", has_citation_id), 
	FOREIGN KEY("Indicator_id") REFERENCES "Indicator" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Citation_has_citation" (
	"Citation_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Citation_id", has_citation_id), 
	FOREIGN KEY("Citation_id") REFERENCES "Citation" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Assertion_predicate" (
	"Assertion_id" TEXT, 
	predicate_id TEXT, 
	PRIMARY KEY ("Assertion_id", predicate_id), 
	FOREIGN KEY("Assertion_id") REFERENCES "Assertion" (id), 
	FOREIGN KEY(predicate_id) REFERENCES "Task" (id)
);
CREATE TABLE "Assertion_subject" (
	"Assertion_id" TEXT, 
	subject_id TEXT, 
	PRIMARY KEY ("Assertion_id", subject_id), 
	FOREIGN KEY("Assertion_id") REFERENCES "Assertion" (id), 
	FOREIGN KEY(subject_id) REFERENCES "Concept" (id)
);
CREATE TABLE "Assertion_predicate_def" (
	"Assertion_id" TEXT, 
	predicate_def_id TEXT, 
	PRIMARY KEY ("Assertion_id", predicate_def_id), 
	FOREIGN KEY("Assertion_id") REFERENCES "Assertion" (id), 
	FOREIGN KEY(predicate_def_id) REFERENCES "Contrast" (id)
);
CREATE TABLE "Assertion_in_theory" (
	"Assertion_id" TEXT, 
	in_theory_id TEXT, 
	PRIMARY KEY ("Assertion_id", in_theory_id), 
	FOREIGN KEY("Assertion_id") REFERENCES "Assertion" (id), 
	FOREIGN KEY(in_theory_id) REFERENCES "Theory" (id)
);
CREATE TABLE "Assertion_has_citation" (
	"Assertion_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Assertion_id", has_citation_id), 
	FOREIGN KEY("Assertion_id") REFERENCES "Assertion" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "User_created" (
	"User_id" TEXT, 
	created_id TEXT, 
	PRIMARY KEY ("User_id", created_id), 
	FOREIGN KEY("User_id") REFERENCES "User" (id), 
	FOREIGN KEY(created_id) REFERENCES "CitableThing" (id)
);
CREATE TABLE "User_has_citation" (
	"User_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("User_id", has_citation_id), 
	FOREIGN KEY("User_id") REFERENCES "User" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "ExternalLink_has_citation" (
	"ExternalLink_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("ExternalLink_id", has_citation_id), 
	FOREIGN KEY("ExternalLink_id") REFERENCES "ExternalLink" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "ConceptClass_has_citation" (
	"ConceptClass_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("ConceptClass_id", has_citation_id), 
	FOREIGN KEY("ConceptClass_id") REFERENCES "ConceptClass" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);
CREATE TABLE "Disambiguation_disambiguates" (
	"Disambiguation_id" TEXT, 
	disambiguates_id TEXT, 
	PRIMARY KEY ("Disambiguation_id", disambiguates_id), 
	FOREIGN KEY("Disambiguation_id") REFERENCES "Disambiguation" (id), 
	FOREIGN KEY(disambiguates_id) REFERENCES "CitableThing" (id)
);
CREATE TABLE "Disambiguation_has_citation" (
	"Disambiguation_id" TEXT, 
	has_citation_id TEXT, 
	PRIMARY KEY ("Disambiguation_id", has_citation_id), 
	FOREIGN KEY("Disambiguation_id") REFERENCES "Disambiguation" (id), 
	FOREIGN KEY(has_citation_id) REFERENCES "Citation" (id)
);