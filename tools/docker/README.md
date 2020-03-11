# MASVS PDFs Generation with Docker

The MASVS document generation is based on pandocker: https://github.com/dalibo/pandocker/blob/latest/LICENSE

## On your Machine

- Install Docker
- `cd` to the MASVS root folder `owasp-masvs/`
- Run the following and give a version number (**do not `cd` into `tools/docker` to run it**):

    ```sh
    $ ./tools/docker/run_docker_masvs_generation_on_local.sh 1.2
    ```

## On GitHub

Each time you push to GitHub the workflows in the [MASVS GitHub Actions](https://github.com/OWASP/owasp-masvs/actions "MASVS GitHub Actions") will be triggered. You can check what will be executed inside the folder `owasp-masvs/.github/workflows`, where `docgenerator.yml` takes care of building the Docker image and running the generation script once per language inside the container.

See the results in: <https://github.com/OWASP/owasp-masvs/actions>

## Generation Steps

Given a new version:

- Build Docker image.
- Run Docker container which will run the generation script (`pandoc_makedocs.sh`).
- The script should be self explanatory, it basically:
  - Reads the LANGUAGE-METADATA for the given VERSION and language folder
  - Using that metadata creates the cover dynamically including language and version (no GIMP required anymore!)
  - For the CJK languages it configures the latex-header file using the right packages and fonts.
  - For more details, read the inline comments in `pandoc_makedocs.sh`.
- The PDFs will be generated in the MASVS root folder.

## Open Points (REMOVE from here when DONE!)

Finish items for [https://github.com/OWASP/owasp-masvs/issues/361](https://github.com/OWASP/owasp-masvs/issues/361):
