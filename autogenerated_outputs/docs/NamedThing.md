
# Class: NamedThing

A generic grouping for any identifiable entity

URI: [legacy_cogat_linkml:NamedThing](https://w3id.org/rwblair/legacy-cogat-linkml/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[CitableThing],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[CitableThing],[CitableThing])

## Children

 * [CitableThing](CitableThing.md)

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a thing
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a thing
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Thing |