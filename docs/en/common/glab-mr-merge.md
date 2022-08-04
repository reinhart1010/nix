---
layout: page
title: common/glab-mr-merge (English)
description: "Merge GitLab merge requests."
content_hash: cae7996afe40ee8be3a1881684853b1ecd91db8c
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># glab mr merge

Merge GitLab merge requests.
More information: <https://glab.readthedocs.io/en/latest/mr/merge.html>.

- Merge the merge request associated with the current branch interactively:

`glab mr merge`

- Merge the specified merge request, interactively:

`glab mr merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mr_number</span>

- Merge the merge request, removing the branch on both the local and the remote:

`glab mr merge --remove-source-branch`

- Squash the current merge request into one commit with the message body and merge:

`glab mr merge --squash --message="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_message_body</span>`"`

- Display help:

`glab mr merge --help`
