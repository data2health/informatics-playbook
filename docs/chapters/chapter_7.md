# Chapter 7: Repository Architecture for Data Discovery

## Intended Audience

This guidance is intended for academic institutional repository stakeholders, such as:  (1) researchers with various goals: finding collaborators, seeking datasets for secondary analysis and teaching, sharing data for compliance with journal and funder mandates, having themselves and their team be recognized for the entirety of their research output (and make that output citable); (2) undergraduate and graduate students for learning and research; (3) support staff who assist researchers in carrying out tasks; and (4) departments, cores, institutions, and consortia who share, aggregate and report data. Next generation institutional repository architecture can meet the needs of all the aforementioned stakeholders and beyond. An example can be seen in the development of InvenioRDM, a turnkey research data management repository.

## Why is this important?

In recent years, expansion of the institution's role in managing research outputs has been associated with increased scientific reproducibility; open science; enhancement of discovery, access, and use of information; increased collaboration and interdisciplinary research; and increased long-term stewardship of scholarly outputs, according to the [MIT Report on the Future of Libraries, 2016](https://future-of-libraries.mit.edu/). This management is frequently accomplished through an “open, trusted, durable, interdisciplinary, and interoperable content platform” that supports research data throughout its lifecycle. The [Confederation of Open Access Repositories (COAR)](https://www.coar-repositories.org/news-updates/what-we-do/next-generation-repositories/), an organization serving repositories and repository networks around the globe, released guiding principles for these platforms in 2018. The recommendations include:

* Distribution of control: distributed control of scholarly outputs, including preprints, post-prints, research data, and supporting software
* Inclusiveness and diversity: allowing for the unique needs of different regions, disciplines and countries
* Public good: technologies, protocols, and architectures of content repositories are available to everyone
* Intelligent openness and accessibility: scholarly resources to be made openly available
* Sustainability: institutional work toward long-term sustainability of resources
* Interoperability: content repositories' employment of functionalities and standards to ensure interoperability across the Web

While institutional repositories can serve as tools employing the six guiding principles, next generation repositories are increasingly enabling far greater interoperability, through both their frameworks and the data and metadata standards they employ, as well as increased support for sustainability and intelligent openness.

In the United States, open science and [FAIR](https://www.force11.org/group/fairgroup/fairprinciples) data practices have been increasingly supported by the scientific community since the 2013 release of a [memo](https://obamawhitehouse.archives.gov/blog/2013/02/22/expanding-public-access-results-federally-funded-research) from the White House [Office of Science and Technology Policy (OSTP)](https://https://www.whitehouse.gov/ostp/) requiring federal agencies with over $100 million in annual conduct of research expenditures to develop plans to increase public access to the results of that research, including research data. While some agencies have set clear guidelines for the repositories to use for housing federally-funded research data, others have left the choice up to the researcher. The [NIH Data Management and Sharing Policy](https://grants.nih.gov/grants/policy/data_sharing/data_sharing_guidance.htm) finalized in Oct 2020 with an effective date of Jan 25, 2023 also leaves the decision up to the researcher as to where to deposit research data for sharing. This policy clearly states the critical role of research data management (RDM) and data sharing:

 ***“Data should be made as widely and freely available as possible while safeguarding the privacy of participants, and protecting confidential and proprietary data.”***

With no shortage of [data repositories](https://journals.plos.org/plosone/s/data-availability#loc-recommended-repositories), researchers require guidance on where their data can best be deposited to maximize access, ensure compliance with journal and funder data sharing requirements, and ensure security and long-term preservation. COAR has released a [Best Practices Framework for Repositories](https://www.coar-repositories.org/coar-community-framework-for-good-practices-in-repositories/) with behaviors that further reflect the needs of researchers when depositing, sharing, and storing data:

* Discovery
* Access
* Reuse
* Integrity and Authenticity
* Quality Assurance
* Privacy of Sensitive Data (e.g. human subjects)
* Preservation
* Sustainability and Governance
* Other Characteristics

These desired behaviors of next generation repositories reflect researchers’ needs to make their research inclusive, participatory, and reproducible. These functions can be enabled through increased interaction with and interoperability of resources; support for commentary and annotation; support for discovery through navigation, user identification, verification, profiles, and alerts; and integration with other systems for managing research output and measuring research impact such as the [Current Research Information System (CRIS) systems](https://nifa.usda.gov/tool/cris).

## Takeaway List

The architecture of a research repository that is able to support emerging research needs meets all the specifications of the next generation repository as outlined above, and is modular and scalable, allowing for improvements in the future based on evolving user needs. InvenioRDM is an exemplar next generation repository, and its modular architecture and strong use of standards helps ensure the ability of the platform to support best practices in research data management. Each record in InvenioRDM is minted a DOI, a permanent identifier exposed through [DataCite](https://datacite.org/) that is available for citation and compliance with data sharing requirements. Robust metadata, an open API, and the powerful Elasticsearch full-text search engine ensures that deposited data is findable, accessible, interoperable, and reusable (FAIR), and also allows for discovery through navigation and batch discovery of resources. As part of the “Reusable” element of FAIR data, licenses are declared with records in InvenioRDM to make the terms of reuse immediately clear. These features of the InvenioRDM architecture support data sharing, innovation, knowledge dissemination, and interdisciplinary collaboration.

Users’ needs are at the heart of the repository architecture of InvenioRDM, and to that end we are implementing specified controls and permissions that allow for identification and authentication of users, including support for [ORCiD](https://orcid.org/) identifiers. InvenioRDM has an open API that makes it easy to share data with external resources, such as CRIS systems. InvenioRDM will provide users with the ability to create Collections, Communities, and shared private records, and will include social features. For ease of use, resource transfer is set up to allow a user to download resources in the same format in which they were uploaded. Industry standard usage statistics are collected for all record pages, including altmetrics, and tracking adheres to General Data Privacy Regulation (GDPR). Finally, the InvenioRDM architecture adheres to the Open Archival Information System (OAIS) standard and allows e.g. the retention of previous versions of records and a robust back-end database employing checksums and fixity checks to ensure long-term preservation of deposited digital files.

To support local RDM, institutions can foster a culture of research data management training, support, and best practices. Resources such as this playbook and guidance provided through informational sessions on responsible conduct of research and data management, data consultations, and support for using a repository solution like InvenioRDM, provided in a systematic way by data-focused professionals, will help researchers manage data throughout the research data lifecycle, from project conception through data collection, processing and analysis, dissemination, and preservation. It is important to emphasize that a repository like InvenioRDM can play a key role in each stage of the data lifecycle by serving as a place to find datasets for preliminary or feasibility studies, a place for researchers to find collaborators for the life of a project, and a place to safely disseminate and preserve data.

To reap the greatest benefits from the next generation repository features of InvenioRDM, create robust records that make the most of their many features, consider these **Top 5 Rules for Depositing Research Object Records**:

1. Make your deposit open access if possible
2. Use the appropriate license, see [Reusable Data Best Practices Chapter 1](../chapters/chapter_1.html)
3. Add [meaningful metadata](https://blog.datacite.org/metadig-recommendations-for-fair-datacite-metadata/) to records
4. Attribute credit where credit is due (attribution chapter link)
5. Make sure you do not include any personal identifiable information (PII) in the record

## Status and Feedback Mechanisms

The next generation repository InvenioRDM was launched with an alpha version at the end of October 2019. The Product Roadmap Overview can be seen [here](https://invenio-software.org/products/rdm/roadmap/), and the Invenio Project Board, outlining future month-long project sprints, can be seen [here](https://github.com/orgs/inveniosoftware/projects). The InvenioRDM team also maintains a public [GitHub site](https://github.com/galterlibrary/InvenioRDM-at-NU) where Issues can be added regarding metadata, user interface requirements, and more.

Daily updates are available on a public [Gitter chat](https://gitter.im/inveniosoftware/InvenioRDM). Monthly updates are made at the Resource Discovery Core meetings (open to the CD2H community) typically held on the last Thursday of the month at 1:00pm ET. The rolling meeting notes can be seen [here](https://docs.google.com/document/d/1vVXuhtwmcOi3Ye9tCwgFaS8KxzX6BT3nqlh5YhuV9Nk/edit?usp=sharing). To contact the InvenioRDM team, please use the CD2H [#InvenioRDM](https://app.slack.com/client/T4SPTQGE7/CGH677GUT/user_profile/UGCFPEPQE) Slack channel.


## Current Version

InvenioRDM enables organizations to securely house research products and make them discoverable, shareable, and citable, from publications and datasets to training materials, software, study materials, lay summaries, policy documents, and more. The platform is being developed as part of a large, multi-organization collaboration which includes the Center for Data to Health (CD2H) in partnership with the European Organization for Nuclear Research (CERN), along with fourteen additional [project partners](https://inveniosoftware.org/blog/2019-04-29-rdm/). It is currently in the alpha release stage, with an [example instance](https://vtfsmghslapps04.fsm.northwestern.edu/) customized for Northwestern University acting as a showcase since October 2019. Another instance for demonstration purposes will be released at CERN in 2020.


## Contributors to this guidebook chapter

Name | site | ORCID
* Sara Gonzales | Northwestern University | 0000-0002-1193-2298
* Lisa O'Keefe | Northwestern University | 0000-0003-1211-7583
* Guillaume Viger | Northwestern University |
* Matt Carson | Northwestern University | 0000-0003-4105-9220
* Tom Morrell | Caltech Library | 0000-0001-9266-5146
* Carlos Fernando Gamboa | Brookhaven National Laboratory
* Lars Holm Nielsen | CERN |
* Kai Wörner | Universität Hamburg | 0000-0001-8939-4437
* Kristi Holmes | Northwestern University | 0000-0001-8420-5254
* Andréa Volz | Oregon Health & Science University | 0000-0002-1438-5664

## Acknowledgments

* [Brookhaven National Laboratory](https://www.bnl.gov/world/)
* [Caltech Library](https://www.library.caltech.edu/)
* [CERN](https://home.cern/)
* [Data Futures](https://www.data-futures.org/)
* [Helmoltz Zentrum Dresden Rossendorf (HZDR)](https://www.hzdr.de/db/Cms?pNid=0)
* [National Center for Data to Health (CD2H)](https://ctsa.ncats.nih.gov/cd2h/)
* Northwestern University Feinberg School of Medicine and [Galter Health Sciences Library](https://galter.northwestern.edu/), DIWG & DIWG Metadata Subcommittee
* [OpenAIRE](https://www.openaire.eu/)
* [TIND](https://tind.io/)
* [Tübitak Ulakbim](https://www.tubitak.gov.tr/en)
* [TU Graz](https://www.tugraz.at/home/)
* [Unversität Hamburg](https://www.fdm.uni-hamburg.de/en.html)
* [WWU Münster](https://www.uni-muenster.de/en/)

## Funding:

This work was supported in part by the CERN Knowledge Transfer Fund, the National Institutes of Health’s National Center for Advancing Translational Sciences CTSA Program Center for Data to Health (Grant U24TR002306), and through the many contributions of the project partners listed at the [InvenioRDM project website](https://inveniosoftware.org/products/rdm/).






