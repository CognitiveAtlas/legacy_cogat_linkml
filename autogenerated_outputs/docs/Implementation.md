
# Class: Implementation



URI: [legacy_cogat_linkml:Implementation](https://w3id.org/rwblair/legacy-cogat-linkml/Implementation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]-%20has_implementation%200..*>[Implementation&#124;implementation_uri:string%20%3F;implementation_name:string%20%3F;implementation_description:string%20%3F;id_task:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ImplementationCollection]++-%20entries%200..*>[Implementation],[CitableThing]^-[Implementation],[Task],[ImplementationCollection],[Citation],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]-%20has_implementation%200..*>[Implementation&#124;implementation_uri:string%20%3F;implementation_name:string%20%3F;implementation_description:string%20%3F;id_task:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[ImplementationCollection]++-%20entries%200..*>[Implementation],[CitableThing]^-[Implementation],[Task],[ImplementationCollection],[Citation],[CitableThing])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[has_implementation](has_implementation.md)*  <sub>0..\*</sub>  **[Implementation](Implementation.md)**
 *  **None** *[➞entries](implementationCollection__entries.md)*  <sub>0..\*</sub>  **[Implementation](Implementation.md)**

## Attributes


### Own

 * [implementation_uri](implementation_uri.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [implementation_name](implementation_name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [implementation_description](implementation_description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id_task](id_task.md)  <sub>0..1</sub>
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
