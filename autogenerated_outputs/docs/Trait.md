
# Class: Trait

Represents a Task

URI: [legacy_cogat_linkml:Trait](https://w3id.org/rwblair/legacy-cogat-linkml/Trait)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Citation]<has_citation(i)%200..*-%20[Trait&#124;definition:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Contrast]<measured_by%200..*-%20[Trait],[ExternalLink]<has_link%200..*-%20[Trait],[TraitCollection]++-%20entries%200..*>[Trait],[CitableThing]^-[Trait],[TraitCollection],[ExternalLink],[Contrast],[Citation],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Citation]<has_citation(i)%200..*-%20[Trait&#124;definition:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Contrast]<measured_by%200..*-%20[Trait],[ExternalLink]<has_link%200..*-%20[Trait],[TraitCollection]++-%20entries%200..*>[Trait],[CitableThing]^-[Trait],[TraitCollection],[ExternalLink],[Contrast],[Citation],[CitableThing])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](traitCollection__entries.md)*  <sub>0..\*</sub>  **[Trait](Trait.md)**

## Attributes


### Own

 * [has_citation](has_citation.md)  <sub>0..\*</sub>
     * Range: [Citation](Citation.md)
 * [has_link](has_link.md)  <sub>0..\*</sub>
     * Range: [ExternalLink](ExternalLink.md)
 * [measured_by](measured_by.md)  <sub>0..\*</sub>
     * Range: [Contrast](Contrast.md)
 * [definition](definition.md)  <sub>0..1</sub>
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
