---
layout: page
title: common/glab-mr (English)
description: "Manage GitLab merge requests from the command-line."
content_hash: 4826752918524daaa997524af49c7f64f215e160
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab mr

Manage GitLab merge requests from the command-line.
Some subcommands such as `glab mr create` have their own usage documentation.
More information: <https://glab.readthedocs.io/en/latest/mr>.

- Create a merge request:

`glab mr create`

- Check out a merge request locally:

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
