
# Class: Assertion



URI: [legacy_cogat_linkml:Assertion](https://w3id.org/rwblair/legacy-cogat-linkml/Assertion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Theory],[Task],[Contrast],[Concept],[Citation],[CitableThing],[Citation]<has_citation(i)%200..*-%20[Assertion&#124;truth_value:string%20%3F;id_subject_def:string%20%3F;user_id:string%20%3F;confidence_level:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Theory]<in_theory%200..*-%20[Assertion],[Contrast]<predicate_def%200..*-%20[Assertion],[Concept]<subject%200..*-%20[Assertion],[Task]<predicate%200..*-%20[Assertion],[AssertionCollection]++-%20entries%200..*>[Assertion],[CitableThing]^-[Assertion],[AssertionCollection])](https://yuml.me/diagram/nofunky;dir:TB/class/[Theory],[Task],[Contrast],[Concept],[Citation],[CitableThing],[Citation]<has_citation(i)%200..*-%20[Assertion&#124;truth_value:string%20%3F;id_subject_def:string%20%3F;user_id:string%20%3F;confidence_level:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Theory]<in_theory%200..*-%20[Assertion],[Contrast]<predicate_def%200..*-%20[Assertion],[Concept]<subject%200..*-%20[Assertion],[Task]<predicate%200..*-%20[Assertion],[AssertionCollection]++-%20entries%200..*>[Assertion],[CitableThing]^-[Assertion],[AssertionCollection])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](assertionCollection__entries.md)*  <sub>0..\*</sub>  **[Assertion](Assertion.md)**

## Attributes


### Own

 * [truth_value](truth_value.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [id_subject_def](id_subject_def.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [user_id](user_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [confidence_level](confidence_level.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [predicate](predicate.md)  <sub>0..\*</sub>
     * Range: [Task](Task.md)
 * [subject](subject.md)  <sub>0..\*</sub>
     * Range: [Concept](Concept.md)
 * [predicate_def](predicate_def.md)  <sub>0..\*</sub>
     * Range: [Contrast](Contrast.md)
 * [in_theory](in_theory.md)  <sub>0..\*</sub>
     * Range: [Theory](Theory.md)
 * [has_citation](has_citation.md)  <sub>0..\*</sub>
     * Range: [Citation](Citation.md)

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
