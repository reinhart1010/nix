---
layout: page
title: common/git-fame (English)
description: "Pretty-print Git repository contributions."
content_hash: 9c7f0f7e864d370b6e6cafd45dcf0d9daa1bd090
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git fame

Pretty-print Git repository contributions.
More information: <https://github.com/casperdcl/git-fame>.

- Calculate contributions for the current Git repository:

`git fame`

- Exclude files/directories that match the specified regular expression:

`git fame --excl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`"`

- Calculate contributions made after the specified date:

`git fame --since "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3 weeks ago|2021-05-13</span>`"`

- Display contributions in the specified format:

`git fame --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pipe|yaml|json|csv|tsv</span>

- Display contributions per file extension:

`git fame --bytype`

- Ignore whitespace changes:

`git fame --ignore-whitespace`

- Detect inter-file line moves and copies:

`git fame -C`

- Detect intra-file line moves and copies:

`git fame -M`
