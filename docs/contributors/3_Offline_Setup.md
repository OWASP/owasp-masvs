# Contribute Offline

For this you need an IDE or text editor and git on your machine.

We recommend using the free [Visual Studio Code editor](https://code.visualstudio.com "Visual Studio Code") with the [markdownlint extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

Read & follow our [style guide](https://github.com/OWASP/owasp-mstg/blob/master/style_guide.md).

## How to Open a PR

1. [Fork the repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).
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
6. [Create a Pull Request (PR)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) (target branch should be `master`).

Your PR will be reviewed soon (refer to this page to learn more about [reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)).

## How to Incorporate the Reviewer's Feedback to your PR

It might be directly approved and merged or one of our reviewers will send you some comments and suggested changes.

When reviewers suggest changes in a pull request, you can automatically incorporate the changes into your PR.

- Revise and if you agree, [apply any Suggested Changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/incorporating-feedback-in-your-pull-request#applying-suggested-changes) using the "Commit suggestions" button.
- In order to process a comment, simply make modifications to the same branch as before and push them to your repository. GitHub will automatically detect these changes and add them to your existing PR.

> NOTE: Remember to regularly [sync your fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) with the upstream repo. This gets you the latest changes and makes easier to merge your PR.
>
>  ```bash
>  git pull upstream/master
>  ```
>

## How to Review a PR

If you'd like to review another contributor's PR please [follow the steps here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request).

### Step 1: Comment and Suggest Changes

You can enter single or multi-line comments (click and drag to select the range of lines):

![Line Comment](https://docs.github.com/assets/cb-1241326/images/help/commits/hover-comment-icon.gif)

**Always prefer making "Suggested Changes"** using the `±` button:

![Suggest Changes](https://docs.github.com/assets/cb-19975/images/help/pull_requests/suggestion-block.png)

If the suggestion you'd like to make cannot be expressed using "suggested changes" please enter a clear comment explaining what should be fixed (e.g. some paragraphs don't link properly or some essential information cannot be found and should be added).

### Step 2: Submit your Review

Once you went through the whole PR you can [submit your review](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request#submitting-your-review)

1. Click on "Review changes".
2. Enter a comment for the contributor.
3. Select the type of review you'd like to leave (Comment, Approve or Request Changes).
4. Click on "Submit review".