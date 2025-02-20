
# Class: Condition

Represents a Task

URI: [legacy_cogat_linkml:Condition](https://w3id.org/rwblair/legacy-cogat-linkml/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Contrast],[Contrast]<has_contrast%200..*-%20[Condition&#124;condition_text:string%20%3F;condition_description:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ConditionCollection]++-%20entries%200..*>[Condition],[Task]-%20has_condition%200..*>[Condition],[CitableThing]^-[Condition],[Task],[ConditionCollection],[Citation],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Contrast],[Contrast]<has_contrast%200..*-%20[Condition&#124;condition_text:string%20%3F;condition_description:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ConditionCollection]++-%20entries%200..*>[Condition],[Task]-%20has_condition%200..*>[Condition],[CitableThing]^-[Condition],[Task],[ConditionCollection],[Citation],[CitableThing])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](conditionCollection__entries.md)*  <sub>0..\*</sub>  **[Condition](Condition.md)**
 *  **None** *[has_condition](has_condition.md)*  <sub>0..\*</sub>  **[Condition](Condition.md)**

## Attributes


### Own

 * [has_contrast](has_contrast.md)  <sub>0..\*</sub>
     * Range: [Contrast](Contrast.md)
 * [condition_text](condition_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [condition_description](condition_description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

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
 * [event_stamp](event_stamp.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id_user](id_user.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [flag_for_curator](flag_for_curator.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
