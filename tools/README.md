# Tools

## Overview

This directory is for tools that are used to generate the necessary files for our release-channels.

Channels:

- Gitbook: currenlty using @sushi2k's repository which is synced manually.
- Github actions & Github releases: We use Github actions to build and verify the documents in an automated fashion as well as build releases.

Files:

- Apply_Link_Check.sh: Tool to inspect the links in the document folders for every language.
- Apply_Lint_Check.sh: Tool to inspect the markdown files their markup in the document folders for every language.
- export.py: Python script to generate a CSV, JSON or XML version of the MASVS.
- masvs.py: Python script used by export.py
- reference.docx: Template file used for generating the word doc using `generate_document.sh`.

## Release process

1. Sync @sushi2k's repository
2. Update the CHANGELOG.md: make sure it says release in every changelog, including the one in the root of the project as well as the CHANGELOG.md for each of the translations! (so no pre-release/RC client, etc.)
3. Commit the changes (with message `Release <version>`)
4. Push a tag with the new version (`git tag -a <version> -m "Release message that will be on github`)
5. Update the Leanpub Files
6. Update OWASP Wiki if necessary
7. Tweet about it with @OWASP-MSTG.

## Adding another language

When you want to add another langauge:

1. Create a folder with the language of choice.
2. Extend `Apply_Link_Check.sh` and `Apply_Linter_Check.sh` with the new folder and make sure you do not end up with dead links or Markdown errors.
3. Update `.github/workflows/checkLint.yml` and add the new folder to the lint checker.
4. Add the `LANGUAGE-METADATA` to the folder.
5. Test the generation of the document by running `tools/docker/run_docker_masvs_generation_on_local.sh` and update `tools/docker/pandoc_makedocs.sh` wherever necessary. See [the docker README.MD for more details on any necessary update processes](docker/README.md).
6. Add the language to the list of languages in `export.py`
7. Update `.github/workflows/docgenerator.yml` and add the action steps for the new language.
8. Update `../LANGS.md` to include the new language.
9. Extend the `../README.md` with the newly available language.
