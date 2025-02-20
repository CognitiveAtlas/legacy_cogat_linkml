
# Class: User



URI: [legacy_cogat_linkml:User](https://w3id.org/rwblair/legacy-cogat-linkml/User)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CitableThing]<created%200..*-%20[User&#124;old_user_id:string%20%3F;username:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UserCollection]++-%20entries%200..*>[User],[CitableThing]^-[User],[UserCollection],[Citation],[CitableThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[CitableThing]<created%200..*-%20[User&#124;old_user_id:string%20%3F;username:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[UserCollection]++-%20entries%200..*>[User],[CitableThing]^-[User],[UserCollection],[Citation],[CitableThing])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](userCollection__entries.md)*  <sub>0..\*</sub>  **[User](User.md)**

## Attributes


### Own

 * [old_user_id](old_user_id.md)  <sub>0..1</sub>
     * Description: The original PHP based site had user ids of the pattern "usr_[[:alnum:]]*". If an id of this kind existed for the user it is stored here.
     * Range: [String](types/String.md)
 * [username](username.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [created](created.md)  <sub>0..\*</sub>
     * Range: [CitableThing](CitableThing.md)

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
