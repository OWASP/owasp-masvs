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
- mstg_parser.py: Python script used by masvs.py to parse the MSTG and generate links to the implementation of MASVS requirements (can be also used standalone).
- reference.docx: Template file used for generating the word doc using `generate_document.sh`.

## Release process

1. Update the CHANGELOG.md in each language directory and add a release statement and summary of the changes since the last release. Update the RECENT_CHANGES.txt in the tools folder. Add it also to the CHANGELOG.md in the root directory.
2. Commit the changes (with message `Release <version>`)
3. Merge the PR into master
4. Checkout master and pull changes:

    ```bash
    $ git checkout master
    $ git pull
    ```

5. Push a tag with the new version:

    ```bash
    $ git tag -a v<version> -m "Release message"
    $ git push origin v<version>
    ```

    > The letter `v` need to be part of the tag name to trigger the release Github action. The tag name will become the version title of the release. The content of the RECENT_CHANGES file will become the body text of the release (be sure it includes the actual title of the release).

6. Verify that Github Action was triggered. The Github action "Upload Release Asset" need to be triggered. This might take 5-10 minutes.
7. Update OWASP Wiki if necessary
8. Tweet about it with @OWASP-MSTG, Linkedin and OWASP Slack

In case something went wrong and we need to remove the release:

1. Delete the tag locally and remotely:

    ```bash
    $ git tag -d <tag>   # delete the tag locally
    $ git push origin :refs/tags/<tag>  # delete the tag remotely
    ```

2. Go to Github release page <https://github.com/OWASP/owasp-masvs/releases>. The release you removed is now in "draft". Click on edit and discard/delete the release.

## Adding another language

When you want to add another language:

1. Create a folder with the language of choice.
2. Extend `Apply_Link_Check.sh` and `Apply_Linter_Check.sh` with the new folder and make sure you do not end up with dead links or Markdown errors.
3. Update `.github/workflows/checkLint.yml` and add the new folder to the lint checker.
4. Add the `LANGUAGE-METADATA` to the folder.
5. Test the generation of the document by running `tools/docker/run_docker_masvs_generation_on_local.sh` and update `tools/docker/pandoc_makedocs.sh` wherever necessary. See [the docker README.MD for more details on any necessary update processes](docker/README.md).
6. Add the language to the list of languages in `export.py`
7. Update `.github/workflows/docgenerator.yml` and add the action steps for the new language.
8. Update `../LANGS.md` to include the new language.
9. Extend the `../README.md` with the newly available language.
