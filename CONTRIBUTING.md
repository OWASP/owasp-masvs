# Contributing

First of all **Create a GitHub account** (a free one is enough) by following [these steps](https://help.github.com/en/articles/signing-up-for-a-new-github-account "Signing up for a new GitHub account").

## How to contribute

A direct contribution to the MASVS can be done in many different ways.

- Create [issues](https://github.com/OWASP/owasp-masvs/issues "MASVS Issues") first for missing requirements, content or errors so that it can be discussed **before** creating a PR.
  - In order to avoid conflicts that several people are working on the same issue without knowing it, the issue will be assigned to one or more people by the project leaders.
  - Explain what you think is missing in the issue, including references (if available) and give a suggestion as to where it could be added.
- **Open a [Pull Request (PR)](https://github.com/OWASP/owasp-masvs/pulls)**.
  - Your PR may be merged after review. Be sure to follow our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md "MSTG Style Guide") when writing content.
  - A PR is the preferred way for small modifications such as correcting typos.
- **Review a [Pull Request (PR)](https://github.com/OWASP/owasp-masvs/pulls)**: If you are a fluent speaker in any of the different languages that the MASVS is available in, feel free to give feedback on any of the submitted PRs.
  > After your PR or issue has been submitted, we will review it as quickly as possible which typically only takes a few days. If you think we have forgotten about it, feel free to give us a nudge after 7 days have passed.
- **Translating the MASVS**: Translating the MASVS in a new language is another great way to contribute.
  - Before starting a translation: contact us on Slack and together we can make sure that you have your co-translator ready.
  - We need a second translator who can verify that the English version of the MASVS has been translated properly.
  - Once you are all set, go to your fork and follow [these steps](tools/README.md#adding-a-new-language) and create a Pull Request once finished.
  > Note that after your translation, we will ask your help to translate any changes as well, so your language can remain up to date. Otherwise we can only create a one-time-release.

## What not to do

Although we greatly appreciate any and all contributions to the project, there are a few things that you should take into consideration:

- The document should not be used as a platform for advertisement of commercial tools, companies or individuals. Write-ups should be written with free and open-source tools in mind and commercial tools are typically not accepted, unless as a reference in the security tools section.
- Unnecessary self-promotion of tools or blog posts is frowned upon. If you have a relation with on of the URLs or tools you are referencing, please state so in the PR so that we can verify that the reference is in line with the rest of the guide.

Please be sure to take a careful look at our [Code of Conduct](https://github.com/OWASP/owasp-mstg/blob/master/CODE_OF_CONDUCT.md "Code of Conduct") for all the details.

## Contribute Online

GitHub makes this extremely easy.

For small changes in one file:

1. Go to the file you'd like to modify and click on "Edit"
2. Do your changes and commit them. GitHub will guide you and suggest to open a Pull Request.

For more complex changes or across files:

1. Simply click "." anywhere on the repo.
2. You'll be welcomed with a "GitHub Codespace" where you can work using an online Visual Studio.
3. Do your changes, commit and push them as you'd do locally.

## Contribute Offline

For this you need an IDE or text editor and git on your machine.

We recommend using the free [Visual Studio Code editor](https://code.visualstudio.com "Visual Studio Code") as it can make use of the code linting feature through the [MarkdownLint plugin](https://github.com/DavidAnson/vscode-markdownlint#install "MarkdownLint plugin"). The code linter can help you when you make mistakes against our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md "MSTG Style Guide"), but be sure to read the style guide yourself, as the code linter will only detect a part of it.

### How to Set Up your Local Contributor Environment

1. Fork the repository. Creating a fork means creating a copy of the repository on your own account, which you can modify without any impact on this repository. GitHub has an [article that describes all the needed steps](https://help.github.com/en/articles/fork-a-repo "Fork a repo").
2. Clone your own repository to your machine so that you can make modifications. If you followed the GitHub tutorial from step 2, you have already done this.
3. Go to the newly cloned directory "owasp-masvs" and add the remote upstream repository:

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

4. Choose what to work on, based on any of the outstanding [issues](https://github.com/OWASP/owasp-masvs/issues "MASVS Issues").
5. Create a branch so that you can cleanly work on the chosen issue: `git checkout -b FixingIssue66`
6. Open your favorite editor and start making modifications.
7. After your modifications are done, push them to your forked repository. This can be done by executing the command `git add MYFILE` for every file you have modified, followed by `git commit -m 'Your Commit Message'` to commit the modifications and `git push` to push your modifications to GitHub.
8. Create a Pull Request (PR) by going to your fork, <https://github.com/Your_Github_Handle/owasp-masvs> and clicking on the "New Pull Request" button. The target branch should typically be the Master branch. When submitting a PR, be sure to follow the checklist that is provided in the PR template. The checklist itself will be filled out by the reviewer.
9. Your PR will be reviewed and comments may be given. In order to process a comment, simply make modifications to the same branch as before and push them to your repository. GitHub will automatically detect these changes and add them to your existing PR.
10. When starting on a new PR in the future, make sure to always keep your local repo up to date:

```bash
git pull upstream/master
```

See also the following article for further explanation on "[How to Keep a Downstream git Repository Current with Upstream Repository Changes](https://medium.com/sweetmeat/how-to-keep-a-downstream-git-repository-current-with-upstream-repository-changes-10b76fad6d97 "How to Keep a Downstream git Repository Current with Upstream Repository Changes")".
