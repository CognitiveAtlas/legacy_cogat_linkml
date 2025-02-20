
# Class: Task

Represents a Task

URI: [legacy_cogat_linkml:Task](https://w3id.org/rwblair/legacy-cogat-linkml/Task)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]<part_of%200..*-%20[Task&#124;id_concept_class:string%20%3F;def_id:string%20%3F;review_status:string%20%3F;def_event_stamp:string%20%3F;def_id_user:string%20%3F;definition_text:string%20%3F;alias:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Task]<kind_of%200..*-%20[Task],[Battery]<in_battery%200..*-%20[Task],[Indicator]<has_indicator%200..*-%20[Task],[Implementation]<has_implementation%200..*-%20[Task],[ExternalDataset]<has_external_dataset%200..*-%20[Task],[Contrast]<has_contrast%200..*-%20[Task],[Condition]<has_condition%200..*-%20[Task],[Concept]<asserts%200..*-%20[Task],[Assertion]-%20predicate%200..*>[Task],[TaskCollection]++-%20entries%200..*>[Task],[CitableThing]^-[Task],[TaskCollection],[Indicator],[Implementation],[ExternalDataset],[Contrast],[Condition],[Concept],[Citation],[CitableThing],[Battery],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]<part_of%200..*-%20[Task&#124;id_concept_class:string%20%3F;def_id:string%20%3F;review_status:string%20%3F;def_event_stamp:string%20%3F;def_id_user:string%20%3F;definition_text:string%20%3F;alias:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Task]<kind_of%200..*-%20[Task],[Battery]<in_battery%200..*-%20[Task],[Indicator]<has_indicator%200..*-%20[Task],[Implementation]<has_implementation%200..*-%20[Task],[ExternalDataset]<has_external_dataset%200..*-%20[Task],[Contrast]<has_contrast%200..*-%20[Task],[Condition]<has_condition%200..*-%20[Task],[Concept]<asserts%200..*-%20[Task],[Assertion]-%20predicate%200..*>[Task],[TaskCollection]++-%20entries%200..*>[Task],[CitableThing]^-[Task],[TaskCollection],[Indicator],[Implementation],[ExternalDataset],[Contrast],[Condition],[Concept],[Citation],[CitableThing],[Battery],[Assertion])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[predicate](predicate.md)*  <sub>0..\*</sub>  **[Task](Task.md)**
 *  **None** *[➞entries](taskCollection__entries.md)*  <sub>0..\*</sub>  **[Task](Task.md)**
 *  **None** *[➞kind_of](task__kind_of.md)*  <sub>0..\*</sub>  **[Task](Task.md)**
 *  **None** *[➞part_of](task__part_of.md)*  <sub>0..\*</sub>  **[Task](Task.md)**

## Attributes


### Own

 * [asserts](asserts.md)  <sub>0..\*</sub>
     * Range: [Concept](Concept.md)
 * [has_condition](has_condition.md)  <sub>0..\*</sub>
     * Range: [Condition](Condition.md)
 * [has_contrast](has_contrast.md)  <sub>0..\*</sub>
     * Range: [Contrast](Contrast.md)
 * [has_external_dataset](has_external_dataset.md)  <sub>0..\*</sub>
     * Range: [ExternalDataset](ExternalDataset.md)
 * [has_implementation](has_implementation.md)  <sub>0..\*</sub>
     * Range: [Implementation](Implementation.md)
 * [has_indicator](has_indicator.md)  <sub>0..\*</sub>
     * Range: [Indicator](Indicator.md)
 * [id_concept_class](id_concept_class.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_id](def_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [review_status](review_status.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_event_stamp](def_event_stamp.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_id_user](def_id_user.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [definition_text](definition_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [in_battery](in_battery.md)  <sub>0..\*</sub>
     * Range: [Battery](Battery.md)
 * [event_stamp](event_stamp.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [alias](alias.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞kind_of](task__kind_of.md)  <sub>0..\*</sub>
     * Range: [Task](Task.md)
 * [➞part_of](task__part_of.md)  <sub>0..\*</sub>
     * Range: [Task](Task.md)

### Inherited from CitableThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)
 * [has_citation](has_citation.md)  <sub>0..\*</sub>
     * Range: [Citation](Citation.md)
 * [last_updated](last_updated.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [creation_time](creation_time.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id_user](id_user.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [flag_for_curator](flag_for_curator.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
