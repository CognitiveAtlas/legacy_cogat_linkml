
# Class: Indicator



URI: [legacy_cogat_linkml:Indicator](https://w3id.org/rwblair/legacy-cogat-linkml/Indicator)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]-%20has_indicator%200..*>[Indicator&#124;type:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Battery]-%20has_indicator%200..*>[Indicator],[IndicatorCollection]++-%20entries%200..*>[Indicator],[CitableThing]^-[Indicator],[Task],[IndicatorCollection],[Citation],[CitableThing],[Battery])](https://yuml.me/diagram/nofunky;dir:TB/class/[Task]-%20has_indicator%200..*>[Indicator&#124;type:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Battery]-%20has_indicator%200..*>[Indicator],[IndicatorCollection]++-%20entries%200..*>[Indicator],[CitableThing]^-[Indicator],[Task],[IndicatorCollection],[Citation],[CitableThing],[Battery])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[has_indicator](has_indicator.md)*  <sub>0..\*</sub>  **[Indicator](Indicator.md)**
 *  **None** *[➞entries](indicatorCollection__entries.md)*  <sub>0..\*</sub>  **[Indicator](Indicator.md)**

## Attributes


### Own

 * [type](type.md)  <sub>0..1</sub>
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
