
# Class: CitableThing

A generic grouping for any identifiable entity

URI: [legacy_cogat_linkml:CitableThing](https://w3id.org/rwblair/legacy-cogat-linkml/CitableThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[User],[Trait],[Theory],[Task],[NamedThing],[Indicator],[Implementation],[ExternalLink],[ExternalDataset],[Disorder],[Disambiguation],[Contrast],[Condition],[ConceptClass],[Concept],[Citation],[Citation]<has_citation%200..*-%20[CitableThing&#124;last_updated:string%20%3F;creation_time:string%20%3F;event_stamp:string%20%3F;id_user:string%20%3F;flag_for_curator:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[User]-%20created%200..*>[CitableThing],[Disambiguation]-%20disambiguates%200..*>[CitableThing],[CitableThing]^-[User],[CitableThing]^-[Trait],[CitableThing]^-[Theory],[CitableThing]^-[Task],[CitableThing]^-[Indicator],[CitableThing]^-[Implementation],[CitableThing]^-[ExternalLink],[CitableThing]^-[ExternalDataset],[CitableThing]^-[Disorder],[CitableThing]^-[Disambiguation],[CitableThing]^-[Contrast],[CitableThing]^-[Condition],[CitableThing]^-[ConceptClass],[CitableThing]^-[Concept],[CitableThing]^-[Citation],[CitableThing]^-[Behavior],[CitableThing]^-[Battery],[CitableThing]^-[Assertion],[NamedThing]^-[CitableThing],[Behavior],[Battery],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[User],[Trait],[Theory],[Task],[NamedThing],[Indicator],[Implementation],[ExternalLink],[ExternalDataset],[Disorder],[Disambiguation],[Contrast],[Condition],[ConceptClass],[Concept],[Citation],[Citation]<has_citation%200..*-%20[CitableThing&#124;last_updated:string%20%3F;creation_time:string%20%3F;event_stamp:string%20%3F;id_user:string%20%3F;flag_for_curator:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[User]-%20created%200..*>[CitableThing],[Disambiguation]-%20disambiguates%200..*>[CitableThing],[CitableThing]^-[User],[CitableThing]^-[Trait],[CitableThing]^-[Theory],[CitableThing]^-[Task],[CitableThing]^-[Indicator],[CitableThing]^-[Implementation],[CitableThing]^-[ExternalLink],[CitableThing]^-[ExternalDataset],[CitableThing]^-[Disorder],[CitableThing]^-[Disambiguation],[CitableThing]^-[Contrast],[CitableThing]^-[Condition],[CitableThing]^-[ConceptClass],[CitableThing]^-[Concept],[CitableThing]^-[Citation],[CitableThing]^-[Behavior],[CitableThing]^-[Battery],[CitableThing]^-[Assertion],[NamedThing]^-[CitableThing],[Behavior],[Battery],[Assertion])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Children

 * [Assertion](Assertion.md)
 * [Battery](Battery.md)
 * [Behavior](Behavior.md) - Represents a Task
 * [Citation](Citation.md)
 * [Concept](Concept.md) - Represents a Task
 * [ConceptClass](ConceptClass.md)
 * [Condition](Condition.md) - Represents a Task
 * [Contrast](Contrast.md) - Represents a Task
 * [Disambiguation](Disambiguation.md)
 * [Disorder](Disorder.md) - Represents a Task
 * [ExternalDataset](ExternalDataset.md)
 * [ExternalLink](ExternalLink.md)
 * [Implementation](Implementation.md)
 * [Indicator](Indicator.md)
 * [Task](Task.md) - Represents a Task
 * [Theory](Theory.md)
 * [Trait](Trait.md) - Represents a Task
 * [User](User.md)

## Referenced by Class

 *  **None** *[created](created.md)*  <sub>0..\*</sub>  **[CitableThing](CitableThing.md)**
 *  **None** *[disambiguates](disambiguates.md)*  <sub>0..\*</sub>  **[CitableThing](CitableThing.md)**

## Attributes


### Own

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

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)
