# Contribute Offline

For this you need an IDE or text editor and git on your machine.

We recommend using the free [Visual Studio Code editor](https://code.visualstudio.com "Visual Studio Code") as it can make use of the code linting feature through the [MarkdownLint plugin](https://github.com/DavidAnson/vscode-markdownlint#install "MarkdownLint plugin"). The code linter can help you when you make mistakes against our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md "MSTG Style Guide"), but be sure to read the style guide yourself, as the code linter will only detect a part of it.

## How to Set Up your Local Contributor Environment

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