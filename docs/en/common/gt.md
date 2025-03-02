---
layout: page
title: common/gt (English)
description: "Create and manage sequences of dependent code changes (stacks) for Git and GitHub."
content_hash: 29e0116c883e1dca987a04681ca300fcc63b3f30
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/gt.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gt

Create and manage sequences of dependent code changes (stacks) for Git and GitHub.
More information: <https://graphite.dev/docs/get-started>.

- Initialise `gt` for the repository in the current directory:

`gt init`

- Create a new branch stacked on top of the current branch and commit staged changes:

`gt create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new commit and fix upstack branches:

`gt modify -cam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message</span>

- Force push all branches in the current stack to GitHub and create or update PRs:

`gt stack submit`

- Checkout different branch (prompts interactive mode when branch name is omitted):

`gt co `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Sync stack with remote version (also deletes merged branches):

`gt sync`

- Log all tracked stacks:

`gt log short`

- Display help for a specified subcommand:

`gt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` --help`
