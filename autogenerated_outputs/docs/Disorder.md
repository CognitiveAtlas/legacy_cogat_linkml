
# Class: Disorder

Represents a Task

URI: [legacy_cogat_linkml:Disorder](https://w3id.org/rwblair/legacy-cogat-linkml/Disorder)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalLink],[ExternalLink]<has_link%200..*-%20[Disorder&#124;classification:string%20%3F;definition:string%20%3F;id_protocol:string%20%3F;is_a_fulltext:string%20%3F;is_a_protocol:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Disorder]<is_a%200..*-%20[Disorder],[DisorderCollection]++-%20entries%200..*>[Disorder],[Contrast]-%20has_difference%200..*>[Disorder],[CitableThing]^-[Disorder],[DisorderCollection],[Contrast],[Citation],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalLink],[ExternalLink]<has_link%200..*-%20[Disorder&#124;classification:string%20%3F;definition:string%20%3F;id_protocol:string%20%3F;is_a_fulltext:string%20%3F;is_a_protocol:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Disorder]<is_a%200..*-%20[Disorder],[DisorderCollection]++-%20entries%200..*>[Disorder],[Contrast]-%20has_difference%200..*>[Disorder],[CitableThing]^-[Disorder],[DisorderCollection],[Contrast],[Citation],[CitableThing])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](disorderCollection__entries.md)*  <sub>0..\*</sub>  **[Disorder](Disorder.md)**
 *  **None** *[has_difference](has_difference.md)*  <sub>0..\*</sub>  **[Disorder](Disorder.md)**
 *  **None** *[is_a](is_a.md)*  <sub>0..\*</sub>  **[Disorder](Disorder.md)**

## Attributes


### Own

 * [classification](classification.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [definition](definition.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [is_a](is_a.md)  <sub>0..\*</sub>
     * Range: [Disorder](Disorder.md)
 * [id_protocol](id_protocol.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [is_a_fulltext](is_a_fulltext.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [is_a_protocol](is_a_protocol.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [is_a](is_a.md)  <sub>0..\*</sub>
     * Range: [Disorder](Disorder.md)
 * [has_link](has_link.md)  <sub>0..\*</sub>
     * Range: [ExternalLink](ExternalLink.md)

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
