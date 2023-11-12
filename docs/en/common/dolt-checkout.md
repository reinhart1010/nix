---
layout: page
title: common/dolt-checkout (English)
description: "Checkout the work tree or tables to a specific branch or commit."
content_hash: b46349e04270dabf0c8350a941455812525c059d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dolt checkout

Checkout the work tree or tables to a specific branch or commit.
More information: <https://github.com/dolthub/dolt>.

- Switch to a branch:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Revert unstaged changes to a table:

`dolt checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table</span>

- Create new branch and switch to it:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create new branch based on a specified commit and switch to it:

`dolt checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
