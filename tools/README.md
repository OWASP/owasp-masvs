# Tools

## Overview

This directory is for tools that are used to generate the necessary files for our release-channels.

Channels:

- Gitbook: currenlty using @sushi2k's repository which is synced manually.
- Github release: currently using travis to automatically build stuff based on a tag. See ../travis.yml. It uses `gendocs.sh`, `generate_document.sh` and `gitbookepubanpdf.sh`.
- Leanpub: `updateLeanpub.sh` is in the making: for now it contains only instructions.

Files:

- Apply_Link_Check.sh: Tool to inspect the links in the document folders for every language.
- Apply_Lint_Check.sh: Tool to inspect the markdown files their markup in the document folders for every language.
- before_install.sh: Script used to install additional tools required for releasing. This script makes sure it only runs when it detects a new tag.
- book.json: The book.json metadata template for Gitbook. Necessary for `gitbookepubanpdf.sh` to automatically create an updated book.json in the root of the folder.
- gendocs.sh: Used to simplify the work with Travis.
- gendocsLocal.sh: Used to do the same as gendocs.sh, but then locally without creating git releases.
- generate_document.sh: Used to generate the docx and html files. (Note _xx is for the given language xx)
- generate_toc.rb: Used to generate a TOC file.
- gitbookepubandpdf.sh: Used to generate the epub, pdf and mobi files.
- export.py: Python script to generate a CSV, JSON or XML version of the MASVS.
- masvs.py: Python script used by export.py
- reference.docx: Template file used for generating the word doc using `generate_document.sh`.

## Release process

1. Sync @sushi2k's repository
2. Update the Changelog.md: make sure it says release in every changelog, including of all the translations! (so no pre-release/RC client, etc.)
3. Commit the changes (with message `Release <version>`)
4. Push a tag with the new version (`git tag -a <version> -m "Release message that will be on github`)
5. Update the Leanpub Files
6. Update OWASP Wiki if necessary
7. Tweet about it with @OWASP-MSTG.

## Adding another language

When you want to add another langauge:

1. Add a `generate_document_[LANG].sh` to the Tools folder
2. Update `gitbookandepubandpdf.sh` with the language referenced
3. Extend `Apply_Link_Check.sh` and `Apply_Linter_Check.sh`
4. Update `gendocs.sh` and `gendoclsLocal.sh` so you can test it locally and see if the markdown land links make sense for the new language. Use this to file issues or report to the translator if fixes are necessary. Please check for pagination as well when you run it so that at release time, you have a proper PDF immediately
5. Extend `../.travis.yml` to include the new language
6. Update `../LANGS.md` to include the new language
7. Extend the `../README.md` with the newly available language
