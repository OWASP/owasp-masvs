# Getting Started

First of all **Create a GitHub account** (a free one is enough) by following [these steps](https://help.github.com/en/articles/signing-up-for-a-new-github-account "Signing up for a new GitHub account").

## Contribute Online

GitHub makes this extremely easy.

For small changes in one file:

1. Go to the file you'd like to modify and [click on "Edit"](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-another-users-repository).
2. Do your changes and commit them. GitHub will guide you and suggest to open a Pull Request.

For more complex changes or across files:

1. Press `.` while browsing the repo or pull request.
2. You'll be welcomed with a ["github.dev Web-based Editor"](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor) where you can work using an online Visual Studio.
3. Do your [changes, commit and push](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#using-source-control) them as you'd do locally.

![github.dev](https://user-images.githubusercontent.com/856858/130119109-4769f2d7-9027-4bc4-a38c-10f297499e8f.gif)

Learn more about the github.dev Web-based Editor in ["GitHub Docs"](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor).

## Contribute Offline

For this you need an IDE or text editor and git on your machine. We recommend using the free [Visual Studio Code editor](https://code.visualstudio.com "Visual Studio Code") with the [markdownlint extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

1. [Fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository). Forking the repo allows you to make your changes without affecting the original project until you're ready to merge them.
2. [Clone your fork repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#about-cloning-a-repository) and [add the remote upstream repo](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#remotes-and-forks), e.g. for owasp-masvs:
    ```bash
    $ git clone https://github.com/<your_github_user>/owasp-masvs.git
    $ git remote add upstream git@github.com:OWASP/owasp-masvs.git
    ```
3. Create a branch.
    ```bash
    $ git checkout -b fix-issue-1456
    ```
4. Make your changes.
5. Commit and push your changes. This can be done by executing the command `git add MYFILE` for every file you have modified, followed by `git commit -m 'Your Commit Message'` to commit the modifications and `git push` to push your modifications to GitHub.
6. [Open a PR](#how-to-open-a-pr).
