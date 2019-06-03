# Tools

## Overview

This directory is for tools that are used to generate the necessary files for our release-channels.

Channels:

- Gitbook: currenlty using @sushi2k's repository which is synced manually.
- Github release: currently using travis to automatically build stuff based on a tag. See ../travis.yml. It uses `gendocs.sh`, `generate_document.sh` and `gitbookepubanpdf.sh`.
- Leanpub: `updateLeanpub.sh` is in the making: for now it contains only instructions.

Files:

- Apply_Link_Check.sh: tool to inspect the links in the document folders for every language.
- Apply_Lint_Check.sh: tool to inspect the markdown files their markup in the document folders for every language.
- before_install.sh: script used to install additional tools required for releasing. This script makes sure it only runs when it detects a new tag.
- book.json: the book.json metadata template for Gitbook. Necessary for `gitbookepubanpdf.sh` to automatically create an updated book.json in the root of the folder.
- gendocs.sh: used to simplify the work with Travis.
- generate_document.sh: used to generate the docx and html files. (Note _xx is for the given language xx)
- generate_toc.rb: used to generate a TOC file.
- gitbookepubandpdf.sh: used to generate the epub, pdf and mobi files.
- masvs.py: old python script to generate some of the MASVS related materials.
- reference.docx: templatefile used for generating the word doc using `generate_document.sh`.

## Release process

1. Sync @sushi2k's repository
2. Update the Changelog.md
3. Commit the changes (with message `Release <version>`)
4. Push a tag with the new version (`git tag -a <version> -m "Release message that will be on github`)
5. Update the Leanpub Files
6. Update OWASP Wiki if necessary
7. Tweet about it with @OWASP-MSTG.
