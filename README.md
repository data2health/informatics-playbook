# informatics playbook
A collaborative guidebook for informatics playbook

The live version is rendered at:

https://reusable-data-best-practices.readthedocs.io

Any new commit push to this repo will trigger a rebuild, so you will see the latest changes from the above URL.

## Chapter Template [DRAFT]
Each chapter should have the following sections:

| Section  | Description |
|  --------|-------------|
|Intended audience | The chapters will cover heterogeous and not necessarily overlapping target audiences; therefore please include a short description to ensure readers' time is wisely spent. |
| Current version / status | Guidance tbd, but some indication of whether the draft is early, actively soliciting comments, or ready to implement |
|Lessons learned / summary | This section is optional but encouraged in chapters where the source of truth for the majority of the content is external (Incorporated here by reference only) | 
|Why this is important| Description of the problem and vision for what best practices will address or make possible|
|Status and feedback mechanisms | What stage is it in the development process? (See options below). Description and links for how people can comment, or contribute -- whether via Google form or GitHub issue etc. |
| Takeaway List | A bulleted list of things you can read and implement (similar to top 10 PLoS Top 10 articles). 
| Deep dive into takeaways | Each item should include specific examples that demonstrate that practice XYZ is possible and offer some insight and *evidence* as to why doing it one way (vs. another) is better. |
| Acknowledgements | Key sources and or contributors. Note that references are most easily incorporated as hyperlinks rather than footnotes. This also makes it easier to read. |

## Chapter status

| Chapter status | What is in it | What the stage means |
| -----|-----|-----|
| Stub | Outline with importance and audience specified | Open for high-level comments |
| Early draft | Outline and preliminary content| Open for community contributions |
| Ready for comment | Mature draft | Actively soliciting more in-depth community feedback |
| Implementation-ready | Mature draft revised in light of input | Ready to be implemented, and evolved according to real world experince with it|

## Add google document to chapters
`main.py` allows you to convert a google document to a markdown file and add it to chapters. To use this run `python main.py <your_google_document_url>`. The images will be downloaded to `docs/_static` and the document will be added to `docs/chapters`.

## Instruction for making changes

### Folder structure
   * This project requires `credentials.json` for the google doc apis to work. This has to be at the root folder of the project. See here how to get the `credentials.json` [https://developers.google.com/docs/api/quickstart/js](https://developers.google.com/docs/api/quickstart/js).
   * Every Sphinx related files are under [docs](docs) folder.
   * [contents.rst](docs/contents.rst) file is the the top-level index page.
   * Each chapter goes under [docs/chapters](docs/chapters) folder. They are markdown files.
   * If you need to include static contents (pictures, css, js files), put it under [docs/_static](docs/_static) folder.

### How to create a new chapter

   * Create a new chapter file with the `.md` extension under [docs/chapters](docs/chapters). Typically you can name it as `chapter_[number]_[brief name].md`.
   * Add your content in Markdown format in this file.
   * If you need to add a media file, upload it to [docs/_static](docs/_static) folder first, and then reference it in your markdown text.
   * Once you are done with the content (you can always come back to make changes later), add the reference to your new chapter file in [docs/contents.rst](docs/contents.rst) file.
   * Every time you commit your changes to github, after a few minutes, your changes will be compiled automatically and rendered on [the live documentation site](https://reusable-data-best-practices.readthedocs.io).

### Option 1: Edit directly on github

### Option 2: Clone the repo and edit locally and then push the changes

## Useful resources:

* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) from Github
* [Using markdown in Sphinx](http://www.sphinx-doc.org/en/master/usage/markdown.html)
  (Sphinx is the documention framework powering this live document)
* [Convert GDoc to Markdown](https://gsuite.google.com/marketplace/app/docs_to_markdown/700168918607)
