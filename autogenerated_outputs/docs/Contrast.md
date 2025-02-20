
# Class: Contrast

Represents a Task

URI: [legacy_cogat_linkml:Contrast](https://w3id.org/rwblair/legacy-cogat-linkml/Contrast)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Disorder],[Disorder]<has_difference%200..*-%20[Contrast&#124;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ContrastCollection]++-%20entries%200..*>[Contrast],[Task]-%20has_contrast%200..*>[Contrast],[Condition]-%20has_contrast%200..*>[Contrast],[Concept]-%20measured_by%200..*>[Contrast],[Trait]-%20measured_by%200..*>[Contrast],[Behavior]-%20measured_by%200..*>[Contrast],[Assertion]-%20predicate_def%200..*>[Contrast],[CitableThing]^-[Contrast],[Trait],[Task],[ContrastCollection],[Condition],[Concept],[Citation],[CitableThing],[Behavior],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Disorder],[Disorder]<has_difference%200..*-%20[Contrast&#124;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ContrastCollection]++-%20entries%200..*>[Contrast],[Task]-%20has_contrast%200..*>[Contrast],[Condition]-%20has_contrast%200..*>[Contrast],[Concept]-%20measured_by%200..*>[Contrast],[Trait]-%20measured_by%200..*>[Contrast],[Behavior]-%20measured_by%200..*>[Contrast],[Assertion]-%20predicate_def%200..*>[Contrast],[CitableThing]^-[Contrast],[Trait],[Task],[ContrastCollection],[Condition],[Concept],[Citation],[CitableThing],[Behavior],[Assertion])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](contrastCollection__entries.md)*  <sub>0..\*</sub>  **[Contrast](Contrast.md)**
 *  **None** *[has_contrast](has_contrast.md)*  <sub>0..\*</sub>  **[Contrast](Contrast.md)**
 *  **None** *[measured_by](measured_by.md)*  <sub>0..\*</sub>  **[Contrast](Contrast.md)**
 *  **None** *[predicate_def](predicate_def.md)*  <sub>0..\*</sub>  **[Contrast](Contrast.md)**

## Attributes


### Own

 * [has_difference](has_difference.md)  <sub>0..\*</sub>
     * Range: [Disorder](Disorder.md)

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
