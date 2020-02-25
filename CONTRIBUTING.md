# Contributing

## How to contribute

A direct contribution to the MASVS can be done in many different ways. As the MASVS is summarizing the requirements outlined in detail in the MSTG, please create [issues](https://github.com/OWASP/owasp-masvs/issues "MASVS Issues") first for missing requirements, content or errors so that it can be discussed **before** creating a PR. In order to avoid conflicts that several people are working on the same issue without knowing it, the issue will be assigned to one or more people by the project leaders.
Explain what you think is missing in the issue, including references (if available) and give a suggestion as to where it could be added.

A [Pull Request (PR)](https://github.com/OWASP/owasp-masvs/pulls "Create a pull request") is a direct contribution to the guide and your PR may be merged after review. Be sure to follow our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md "MSTG Style Guide") when writing content. A PR is the preferred way for small modifications such as correcting typos. If you are a fluent speaker in any of the different languages that the MASVS is available in, feel free to give feedback on any of the submitted PRs.

After your PR or issue has been submitted, we will review it as quickly as possible which typically only takes a few days. If you think we have forgotten about it, feel free to give us a nudge after 7 days have passed.

## How to set up my contributor environment

1. Create a GitHub account. Multiple different GitHub subscription plans are available, but you only need a free one. Follow [these steps](https://help.github.com/en/articles/signing-up-for-a-new-github-account "Signing up for a new GitHub account") to set up your account.
2. Fork the repository. Creating a fork means creating a copy of the repository on your own account, which you can modify without any impact on this repository. GitHub has an [article that describes all the needed steps](https://help.github.com/en/articles/fork-a-repo "Fork a repo").
3. Clone your own repository to your machine so that you can make modifications. If you followed the GitHub tutorial from step 2, you have already done this.
4. Go to the newly cloned directory "owasp-masvs" and add the remote upstream repository:

    ```bash
    $ git remote -v
    origin git@github.com:<your Github handle>/owasp-masvs.git (fetch)
    origin git@github.com:<your Github handle>/owasp-masvs.git (push)
    $ git remote add upstream git@github.com:OWASP/owasp-masvs.git
    $ git remote -v
    origin git@github.com:<your Github handle>/owasp-masvs.git (fetch)
    origin git@github.com:<your Github handle>/owasp-masvs.git (push)
    upstream git@github.com:OWASP/owasp-masvs.git (fetch)
    upstream git@github.com:OWASP/owasp-masvs.git (push)
    ```

    See also the GitHub documentation on [Configuring a remote for a fork](https://help.github.com/en/articles/configuring-a-remote-for-a-fork "Configuring a remote for a fork").

5. Choose what to work on, based on any of the outstanding [issues](https://github.com/OWASP/owasp-masvs/issues "MASVS Issues").
6. Create a branch so that you can cleanly work on the chosen issue: `git checkout -b FixingIssue66`
7. Open your favorite editor and start making modifications. We recommend using the free [Visual Studio Code editor](https://code.visualstudio.com "Visual Studio Code") as it can make use of the code linting feature through the [MarkdownLint plugin](https://github.com/DavidAnson/vscode-markdownlint#install "MarkdownLint plugin"). The code linter can help you when you make mistakes against our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md "MSTG Style Guide"), but be sure to read the style guide yourself, as the code linter will only detect a part of it.
8. After your modifications are done, push them to your forked repository. This can be done by executing the command `git add MYFILE` for every file you have modified, followed by `git commit -m 'Your Commit Message'` to commit the modifications and `git push` to push your modifications to GitHub. Protip, use the issue-ID in your commit message (e.g. `#<issueNumber>`).
9. Create a Pull Request (PR) by going to your fork, <https://github.com/Your_Github_Handle/owasp-masvs> and clicking on the "New Pull Request" button. The target branch should typically be the Master branch. When submitting a PR, be sure to follow the checklist that is provided in the PR template. The checklist itself will be filled out by the reviewer.
10. Your PR will be reviewed and comments may be given. In order to process a comment, simply make modifications to the same branch as before and push them to your repository. GitHub will automatically detect these changes and add them to your existing PR.
11. When starting on a new PR in the future, make sure to always keep your local repo up to date:

```bash
$ git fetch upstream
$ git merge upstream/master
```

See also the following article for further explanation on "[How to Keep a Downstream git Repository Current with Upstream Repository Changes](https://medium.com/sweetmeat/how-to-keep-a-downstream-git-repository-current-with-upstream-repository-changes-10b76fad6d97 "How to Keep a Downstream git Repository Current with Upstream Repository Changes")".

## Translating

Our current goal is to publish one minor release every 6 months. Next, we will often create patch updates in order to provide intermediary updates in PDF and DocX format. Releases that have been tagged can then be translated into preferred languages. (Note we use semantic versioning: major.minor.patch)

### Start new translation

Translating the MASVS in a new language is great, but given the nature of the MASVS, we have to make sure that the translation can be verified by a second translator who can verify that the English version of the MASVS has been translated properly. So when you want to start a translation: contact us on Slack and together we can make sure that you have your co-translator ready. Once you are all set, we execute the following steps:

1. Follow step 1-8 of [How to set up my contributor environment](##How to set up my contributor environment).
2. Create a pull request for the langauge you want to support. All you have to do is create a copy of the `Document` folder and commit it, annotated with the language of your choice. For instance, if you want to translate the document into Dutch (NL), you create a copy of the `Document` folder and commit it as `Document-nl`.
3. Start the actual translation, one PR after another, which then needs to be reviewed by your fellow translator. Try to do this 1 chapter per PR, so that the reviewer can give feedback on short submissions without being overwhelmed.
4. When you have started with 3, contact us, so we can help you with the necessary scripts to automatically generate PDFS/Epubs/Mobi files so you can see how your translation looks in those formats.
5. Once all the chapters are translated, we can start creating a release.

Note that after your translation, we will ask your help to translate any changes as well, so your language can remain up to date. Otherwise we can only create a one-time-release.

## What not to do

Although we greatly appreciate any and all contributions to the project, there are a few things that you should take into consideration:

- The MASVS should not be used as a platform for advertisement of commercial tools, companies or individuals. Any contribution should be written with free and open-source tools in mind and commercial tools are typically not accepted.
- Unnecessary self-promotion of tools or blog posts is frowned upon. If you have a relation with on of the URLs or tools you are referencing, please state so in the PR so that we can verify that the reference is in line with the rest of the guide.

## One last note regarding the tables

To make sure that the tables look nicely, we make use of the unicode character `U+00A0` to format the tables correctly. If you want to translate the table: just copy it and change the content, but let the "trailing spaces" remain untouched. Similarly when you add a new requirement: just copy the final requirement of a table and change the content into the new requirement.
