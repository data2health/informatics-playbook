# Developer guide

## Folder structure
The **basicstrap** folder contains all the relevant css and html templates. This is essentially the sphinx theme used for this project.

The **docs** folder contains all the relevant sphinx configs as well as this projects specific landing page (`index.html`).

The **scripts** folder contains the script that converts a given google doc file to an md file and places it under **folder/chapters**.

The **ui** folder contains all the necessary vue components and configs that are needed to build the final webapp.

## Development

Each time you change a file under **basicstrap** you need to run `make html` in the **docs** so that sphinx rebuilds the project with the changes.

Each time you change a file under **ui** you need to run `yarn build` in the **ui** so that vue builds the bundles which are outputted to *basicstrap/templates/basicstrap/static/vue*. Then you need to run `make html` again so that sphinx to picks up the generated bundles. The picking up happens in the **docs/conf.py** file.