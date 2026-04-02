# zebrafish-toxicology-atlas-schema

Schema to represent metadata associated with the Zebrafish Toxicology Atlas

## Website

[https://zappfish.org/zebrafish-toxicology-atlas-schema/](https://sierra-moxon.github.io/zebrafish-toxicology-atlas-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [zebrafish_toxicology_atlas_schema](src/zebrafish_toxicology_atlas_schema)
    * [schema](src/zebrafish_toxicology_atlas_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/zebrafish_toxicology_atlas_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
