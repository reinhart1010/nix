---
layout: page
title: common/dolt-checkout (English)
description: "Checkout the work tree or tables to a specific branch or commit."
content_hash: 2e2ce0fa93e361d40a003c8fee439a4a79eef41e
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt checkout

Checkout the work tree or tables to a specific branch or commit.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>.

- Switch to a branch:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Revert unstaged changes to a table:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Create new branch and switch to it:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create new branch based on a specified commit and switch to it:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
