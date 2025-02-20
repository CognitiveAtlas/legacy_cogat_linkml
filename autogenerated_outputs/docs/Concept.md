
# Class: Concept

Represents a Task

URI: [legacy_cogat_linkml:Concept](https://w3id.org/rwblair/legacy-cogat-linkml/Concept)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Contrast],[ConceptClass],[ConceptClass]<classified_under%200..*-%20[Concept&#124;alias:string%20%3F;id_concept_class:string%20%3F;def_id:string%20%3F;def_event_stamp:string%20%3F;def_id_user:string%20%3F;definition_text:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Contrast]<measured_by%200..*-%20[Concept],[Concept]<kind_of%200..*-%20[Concept],[Concept]<part_of%200..*-%20[Concept],[Task]-%20asserts%200..*>[Concept],[ConceptCollection]++-%20entries%200..*>[Concept],[Assertion]-%20subject%200..*>[Concept],[CitableThing]^-[Concept],[Task],[ConceptCollection],[Citation],[CitableThing],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[Contrast],[ConceptClass],[ConceptClass]<classified_under%200..*-%20[Concept&#124;alias:string%20%3F;id_concept_class:string%20%3F;def_id:string%20%3F;def_event_stamp:string%20%3F;def_id_user:string%20%3F;definition_text:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Contrast]<measured_by%200..*-%20[Concept],[Concept]<kind_of%200..*-%20[Concept],[Concept]<part_of%200..*-%20[Concept],[Task]-%20asserts%200..*>[Concept],[ConceptCollection]++-%20entries%200..*>[Concept],[Assertion]-%20subject%200..*>[Concept],[CitableThing]^-[Concept],[Task],[ConceptCollection],[Citation],[CitableThing],[Assertion])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[asserts](asserts.md)*  <sub>0..\*</sub>  **[Concept](Concept.md)**
 *  **None** *[➞entries](conceptCollection__entries.md)*  <sub>0..\*</sub>  **[Concept](Concept.md)**
 *  **None** *[kind_of](kind_of.md)*  <sub>0..\*</sub>  **[Concept](Concept.md)**
 *  **None** *[part_of](part_of.md)*  <sub>0..\*</sub>  **[Concept](Concept.md)**
 *  **None** *[subject](subject.md)*  <sub>0..\*</sub>  **[Concept](Concept.md)**

## Attributes


### Own

 * [alias](alias.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [part_of](part_of.md)  <sub>0..\*</sub>
     * Range: [Concept](Concept.md)
 * [kind_of](kind_of.md)  <sub>0..\*</sub>
     * Range: [Concept](Concept.md)
 * [measured_by](measured_by.md)  <sub>0..\*</sub>
     * Range: [Contrast](Contrast.md)
 * [classified_under](classified_under.md)  <sub>0..\*</sub>
     * Range: [ConceptClass](ConceptClass.md)
 * [id_concept_class](id_concept_class.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_id](def_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_event_stamp](def_event_stamp.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [def_id_user](def_id_user.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [definition_text](definition_text.md)  <sub>0..1</sub>
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
