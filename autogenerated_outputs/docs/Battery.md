
# Class: Battery



URI: [legacy_cogat_linkml:Battery](https://w3id.org/rwblair/legacy-cogat-linkml/Battery)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Indicator],[Citation],[CitableThing],[Citation]<has_citation(i)%200..*-%20[Battery&#124;collection:string%20%3F;collection_description:string%20%3F;collection_alias:string%20%3F;collection_date_introduced:string%20%3F;collection_publisher:string%20%3F;website:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Battery]<part_of%200..*-%20[Battery],[Battery]<kind_of%200..*-%20[Battery],[Battery]<in_battery%200..*-%20[Battery],[Indicator]<has_indicator%200..*-%20[Battery],[BatteryCollection]++-%20entries%200..*>[Battery],[CitableThing]^-[Battery],[BatteryCollection])](https://yuml.me/diagram/nofunky;dir:TB/class/[Indicator],[Citation],[CitableThing],[Citation]<has_citation(i)%200..*-%20[Battery&#124;collection:string%20%3F;collection_description:string%20%3F;collection_alias:string%20%3F;collection_date_introduced:string%20%3F;collection_publisher:string%20%3F;website:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Battery]<part_of%200..*-%20[Battery],[Battery]<kind_of%200..*-%20[Battery],[Battery]<in_battery%200..*-%20[Battery],[Indicator]<has_indicator%200..*-%20[Battery],[BatteryCollection]++-%20entries%200..*>[Battery],[CitableThing]^-[Battery],[BatteryCollection])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](batteryCollection__entries.md)*  <sub>0..\*</sub>  **[Battery](Battery.md)**
 *  **None** *[➞kind_of](battery__kind_of.md)*  <sub>0..\*</sub>  **[Battery](Battery.md)**
 *  **None** *[➞part_of](battery__part_of.md)*  <sub>0..\*</sub>  **[Battery](Battery.md)**
 *  **None** *[in_battery](in_battery.md)*  <sub>0..\*</sub>  **[Battery](Battery.md)**

## Attributes


### Own

 * [collection](collection.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [collection_description](collection_description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [collection_alias](collection_alias.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has_citation](has_citation.md)  <sub>0..\*</sub>
     * Range: [Citation](Citation.md)
 * [has_indicator](has_indicator.md)  <sub>0..\*</sub>
     * Range: [Indicator](Indicator.md)
 * [in_battery](in_battery.md)  <sub>0..\*</sub>
     * Range: [Battery](Battery.md)
 * [collection_date_introduced](collection_date_introduced.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [collection_publisher](collection_publisher.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [website](website.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞kind_of](battery__kind_of.md)  <sub>0..\*</sub>
     * Range: [Battery](Battery.md)
 * [➞part_of](battery__part_of.md)  <sub>0..\*</sub>
     * Range: [Battery](Battery.md)

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
