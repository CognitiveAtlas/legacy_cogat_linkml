
# Class: Theory



URI: [legacy_cogat_linkml:Theory](https://w3id.org/rwblair/legacy-cogat-linkml/Theory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Theory]<part_of%200..*-%20[Theory&#124;collection_description:string%20%3F;collection_alias:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Theory]<kind_of%200..*-%20[Theory],[Assertion]-%20in_theory%200..*>[Theory],[TheoryCollection]++-%20entries%200..*>[Theory],[CitableThing]^-[Theory],[TheoryCollection],[Citation],[CitableThing],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Theory]<part_of%200..*-%20[Theory&#124;collection_description:string%20%3F;collection_alias:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Theory]<kind_of%200..*-%20[Theory],[Assertion]-%20in_theory%200..*>[Theory],[TheoryCollection]++-%20entries%200..*>[Theory],[CitableThing]^-[Theory],[TheoryCollection],[Citation],[CitableThing],[Assertion])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[in_theory](in_theory.md)*  <sub>0..\*</sub>  **[Theory](Theory.md)**
 *  **None** *[➞entries](theoryCollection__entries.md)*  <sub>0..\*</sub>  **[Theory](Theory.md)**
 *  **None** *[➞kind_of](theory__kind_of.md)*  <sub>0..\*</sub>  **[Theory](Theory.md)**
 *  **None** *[➞part_of](theory__part_of.md)*  <sub>0..\*</sub>  **[Theory](Theory.md)**

## Attributes


### Own

 * [collection_description](collection_description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [collection_alias](collection_alias.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞kind_of](theory__kind_of.md)  <sub>0..\*</sub>
     * Range: [Theory](Theory.md)
 * [➞part_of](theory__part_of.md)  <sub>0..\*</sub>
     * Range: [Theory](Theory.md)

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
