# reusable-data-best-practices
A collaborative guidebook for reusable data best practices

The live version is rendered at:

https://reusable-data-best-practices.readthedocs.io

Any new commit push to this repo will trigger a rebuild, so you will see the latest changes from the above URL.

## Chapter Template [DRAFT]
Each chapter should have the following sections:

| Section  | Description |
|  --------|-------------|
|Intended audience | The chapters will cover heterogeous and not necessarily overlapping target audiences; therefore please include a short description to ensure readers' time is wisely spent. |
| Current version / status | Guidance tbd, but some indication of whether the draft is early, actively soliciting comments, or ready to implement |
|Why this is important| Description of the problem and vision for what best practices will address or make possible|
|Status and feedback mechanisms | What stage is it in the development process? (See options below). Description and links for how people can comment, or contribute -- whether via Google form or GitHub issue etc. |
| Takeaway List | A bulleted list of things you can read and implement (similar to top 10 PLoS Top 10 articles). 
| Deep dive into takeaways | Each item should include specific examples that demonstrate that practice XYZ is possible and offer some insight as to why doing it one way (vs. another) is better. |
|Lessons learned / summary | This section is optional but encouraged in chapters where the source of truth for the majority of the content is external (Incorporated here by reference only) | 
| Acknowledgements | Key sources and or contributors. Note that references are most easily incorporated as hyperlinks rather than footnotes. This also makes it easier to read. |

## Chapter status

| Chapter status | What is in it | What the stage means |
| -----|-----|-----|
| Stub | Outline with importance and audience specified | Open for high-level comments |
| Early draft | Outline and preliminary content| Open for community contributions |
| Ready for comment | Mature draft | Actively soliciting more in-depth community feedback |
| Implementation-ready | Mature draft revised in light of input | Ready to be implemented, and evolved according to real world experince with it|

## Instruction for making changes

### Folder structure
   * Every Sphinx related files are under [docs](docs) folder.
   * [index.rst](docs/index.rst) file is the the top-level index page.
   * Each chapter goes under [docs/chapters](docs/chapters) folder. They are markdown files.
   * If you need to include static contents (pictures, css, js files), put it under [docs/_static](_docs/static) folder.

### Option 1: Edit directly on github

### Option 2: Clone the repo and edit locally and then push the changes




