# Chapter 2: Best practices for Using Identifiers

## Intended audience

We propose actions that identifier practitioners (public database providers) should take in the design, provision, and reuse of identifiers. We also outline important considerations for those referencing identifiers in various circumstances, including by authors and data generators. While the importance and relevance of each lesson will vary by context, there is a need for increased awareness about how to avoid and manage common identifier problems, especially those related to persistence and web-accessibility/resolvability. We focus strongly on web-based identifiers in the life sciences; however, the principles are broadly relevant to other disciplines. Although the lessons are most relevant to publicly-accessible research data, there are transferrable principles for private data as well.

## Why is this important?

The issue is as old as scholarship itself: readers have always required persistent identifiers in order to efficiently and reliably retrieve cited works. “Desultory citation practices” have been [thwarting scholarship for millennia](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio.2001414.ref001) either because reliable identifiers were unavailable or because authors failed to use them. While the internet has revolutionized the efficiency of retrieving sources, the same cannot be said for reliability; it is well established that a [significant percentage of cited web addresses go "dead"](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio.2001414.ref002). This process is commonly referred to as "link rot" because availability of cited works [decays with time](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414#pbio.2001414.ref003). Although link rot threatens to erode the utility and reproducibility of scholarship, it is not inevitable; link persistence has been the recognized solution since the dawn of the internet. However, this problem, as we will discuss, is not at all limited to referencing journal articles. The life sciences have changed a lot over the past decade as data have evolved to be ever larger, more distributed, more interdependent, and more natively web-based. This transformation has fundamentally altered what it even means to “reference” a resource; it has diversified both the actors doing the referencing and the entities being referenced. Moreover, the challenges are compounded by a lack of shared terminology about what an “identifier” even is.

## Status and contribution mechanisms
This chapter is [implementation-ready](https://github.com/data2health/reusable-data-best-practices/blob/master/README.md#stages). We welcome feedback, whether by way of [github issue](https://github.com/data2health/reusable-data-best-practices/issues), [google form](https://docs.google.com/forms/d/e/1FAIpQLSfN8R7Hj3qpf-Cek2O0sA3Uaxr3IaFp-iQ_tVI0f4EsgHxU7g/viewform), or [email us](mailto:data2health@gmail.com).

## Takeaways

The list of lessons is below; [the paper from which they are derived contains examples and rationale for each one.](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414)

#### Lesson 1. Credit any derived content using its original identifier
#### Lesson 2. Help local IDs travel well; document prefix and patterns
#### Lesson 3. Opt for simple, durable web resolution
#### Lesson 4. Avoid embedding meaning or relying on it for uniqueness
#### Lesson 5. Design new identifiers for diverse uses by others
#### Lesson 6. Implement a version-management policy
#### Lesson 7. Do not reassign or delete identifiers
#### Lesson 8. Make URIs clear and findable
#### Lesson 9. Document the identifiers you issue and use
#### Lesson 10. Reference and display responsibly


Better identifier design, provisioning, documentation, and referencing can address many of the identifier problems encountered in the life science data cycle, leading to more efficient and effective science. However, best practices will not be adopted on the basis of their community benefit alone; the practices must be both easy and rewarding to the groups that do the implementing. In the broader context of scholarly publishing, this is just what DOIs afford; DOIs succeeded because they were well aligned with journals’ business goals (tracking citations) and because the cost was worth it to them. However, in the current world where everyone is a data provider, alignment with business goals is still being explored. Meta resolvers can provide a use case for journals and websites seeking easier access to content, while software applications leverage these identifier links to mine for knowledge.

We recognize that improvements to the quality, diversity, and uptake of identifier tooling would lower barriers to adoption of the lessons presented here. Those that issue data identifiers face different challenges than do those referencing data identifiers. We understand there are ecosystem-wide challenges and we will address these gaps in the relevant initiatives. We also recognize the need for formal software-engineering specifications of identifier formats and/or alignment between existing specifications. Here, we implore all participants in the scholarly ecosystem—authors, data creators, data integrators, publishers, software developers, resolvers—to aid in the dream of identifier harmony and hope that this playbook can catalyze such efforts.

## Acknowledgments

The content of this chapter was derived from [the following paper](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2001414), an open access article distributed under the terms of the Creative Commons Attribution License that permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Numerous funding sources were involved in supporting this effort, most notably, BioMedBridges and the Monarch Initiative; however, all of the sources are listed in the paper.

- Julie A. McMurry, Nick Juty, Niklas Blomberg, Tony Burdett, Tom Conlin, Nathalie Conte, Mélanie Courtot, John Deck, Michel Dumontier, Donal K. Fellows, Alejandra Gonzalez-Beltran, Philipp Gormanns, Jeffrey Grethe, Janna Hastings, Jean-Karim Hériché, Henning Hermjakob, Jon C. Ison, Rafael C. Jimenez, Simon Jupp, John Kunze, Camille Laibe, Nicolas Le Novère, James Malone, Maria Jesus Martin, Johanna R. McEntyre, Chris Morris, Juha Muilu, Wolfgang Müller, Philippe Rocca-Serra, Susanna-Assunta Sansone, Murat Sariyar, Jacky L. Snoep, Stian Soiland-Reyes, Natalie J. Stanford, Neil Swainston, Nicole Washington, Alan R. Williams, Sarala M. Wimalaratne, Lilly M. Winfree, Katherine Wolstencroft, Carole Goble, Christopher J. Mungall, Melissa A. Haendel, Helen Parkinson. Identifiers for the 21st century: How to design, provision, and reuse persistent identifiers to maximize utility and impact of life science data. *PLoS Bio.* 2017. https://doi.org/10.1371/journal.pbio.2001414


