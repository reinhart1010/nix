---
layout: page
title: common/glab-mr (English)
description: "Manage GitLab merge requests."
content_hash: 9d7e48df83840731a0ea8517c138fd083143d093
last_modified_at: 2024-10-05
tldri18n_status: 2
---
# glab mr

Manage GitLab merge requests.
Some subcommands such as `create` have their own usage documentation.
More information: <https://glab.readthedocs.io/en/latest/mr>.

- Create a merge request:

`glab mr create`

- Check out a specific merge request locally:

`glab mr checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_number</span>

- View the changes made in the merge request:

`glab mr diff`

- Approve the merge request for the current branch:

`glab mr approve`

- Merge the merge request associated with the current branch interactively:

`glab mr merge`

- Edit a merge request interactively:

`glab mr update`

- Edit the target branch of a merge request:

`glab mr update --target-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
