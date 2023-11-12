---
layout: page
title: common/hub (English)
description: "A wrapper for Git that adds commands for working with GitHub-based projects."
content_hash: fc05acc38ae1d749c87ee90b49e53cd26d9b0484
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hub

A wrapper for Git that adds commands for working with GitHub-based projects.
If set up as instructed by `hub alias`, one can use `git` to run `hub` commands.
More information: <https://hub.github.com>.

- Clone a repository using its slug (owners can omit the username):

`hub clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_name</span>

- Create a fork of the current repository (cloned from another user) under your GitHub profile:

`hub fork`

- Push the current local branch to GitHub and create a PR for it in the original repository:

`hub push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` && hub pull-request`

- Create a PR of the current (already pushed) branch, reusing the message from the first commit:

`hub pull-request --no-edit`

- Create a new branch with the contents of a pull request and switch to it:

`hub pr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number</span>

- Upload the current (local-only) repository to your GitHub account:

`hub create`

- Fetch Git objects from upstream and update local branches:

`hub sync`
