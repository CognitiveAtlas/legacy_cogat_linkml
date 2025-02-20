
# Class: Citation



URI: [legacy_cogat_linkml:Citation](https://w3id.org/rwblair/legacy-cogat-linkml/Citation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CitationCollection]++-%20entries%200..*>[Citation&#124;citation_url:string%20%3F;citation_comment:string%20%3F;citation_desc:string%20%3F;citation_authors:string%20%3F;citation_type:string%20%3F;citation_pubname:string%20%3F;citation_pubdate:string%20%3F;citation_pmid:string%20%3F;citation_source:string%20%3F;doi:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[CitableThing]-%20has_citation%200..*>[Citation],[Trait]-%20has_citation(i)%200..*>[Citation],[Behavior]-%20has_citation(i)%200..*>[Citation],[Battery]-%20has_citation(i)%200..*>[Citation],[Assertion]-%20has_citation(i)%200..*>[Citation],[CitableThing]^-[Citation],[Trait],[CitationCollection],[CitableThing],[Behavior],[Battery],[Assertion])](https://yuml.me/diagram/nofunky;dir:TB/class/[CitationCollection]++-%20entries%200..*>[Citation&#124;citation_url:string%20%3F;citation_comment:string%20%3F;citation_desc:string%20%3F;citation_authors:string%20%3F;citation_type:string%20%3F;citation_pubname:string%20%3F;citation_pubdate:string%20%3F;citation_pmid:string%20%3F;citation_source:string%20%3F;doi:string%20%3F;last_updated(i):string%20%3F;creation_time(i):string%20%3F;event_stamp(i):string%20%3F;id_user(i):string%20%3F;flag_for_curator(i):string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[CitableThing]-%20has_citation%200..*>[Citation],[Trait]-%20has_citation(i)%200..*>[Citation],[Behavior]-%20has_citation(i)%200..*>[Citation],[Battery]-%20has_citation(i)%200..*>[Citation],[Assertion]-%20has_citation(i)%200..*>[Citation],[CitableThing]^-[Citation],[Trait],[CitationCollection],[CitableThing],[Behavior],[Battery],[Assertion])

## Parents

 *  is_a: [CitableThing](CitableThing.md)

## Referenced by Class

 *  **None** *[➞entries](citationCollection__entries.md)*  <sub>0..\*</sub>  **[Citation](Citation.md)**
 *  **None** *[has_citation](has_citation.md)*  <sub>0..\*</sub>  **[Citation](Citation.md)**

## Attributes


### Own

 * [citation_url](citation_url.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_comment](citation_comment.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_desc](citation_desc.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_authors](citation_authors.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_type](citation_type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_pubname](citation_pubname.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_pubdate](citation_pubdate.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_pmid](citation_pmid.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [citation_source](citation_source.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [doi](doi.md)  <sub>0..1</sub>
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
