
# Class: ExternalLink



URI: [legacy_cogat_linkml:ExternalLink](https://w3id.org/rwblair/legacy-cogat-linkml/ExternalLink)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalLinkCollection]++-%20entries%200..*>[ExternalLink&#124;uri:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Disorder]-%20has_link%200..*>[ExternalLink],[Trait]-%20has_link%200..*>[ExternalLink],[Behavior]-%20has_link%200..*>[ExternalLink],[CitableThing]^-[ExternalLink],[Trait],[ExternalLinkCollection],[Disorder],[Citation],[CitableThing],[Behavior])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExternalLinkCollection]++-%20entries%200..*>[ExternalLink&#124;uri:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Disorder]-%20has_link%200..*>[ExternalLink],[Trait]-%20has_link%200..*>[ExternalLink],[Behavior]-%20has_link%200..*>[ExternalLink],[CitableThing]^-[ExternalLink],[Trait],[ExternalLinkCollection],[Disorder],[Citation],[CitableThing],[Behavior])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](externalLinkCollection__entries.md)*  <sub>0..\*</sub>  **[ExternalLink](ExternalLink.md)**
 *  **None** *[has_link](has_link.md)*  <sub>0..\*</sub>  **[ExternalLink](ExternalLink.md)**

## Attributes


### Own

 * [uri](uri.md)  <sub>0..1</sub>
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
