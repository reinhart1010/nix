---
layout: page
title: common/rbt (English)
description: "RBTools is a set of command-line tools for working with Review Board and RBCommons."
content_hash: 62c7a8d411e2fe640c063e5dbd64753e527ab0be
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rbt

RBTools is a set of command-line tools for working with Review Board and RBCommons.
More information: <https://www.reviewboard.org/docs/rbtools/dev/>.

- Post changes to Review Board:

`rbt post `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">change_number</span>

- Display the diff that will be sent to Review Board:

`rbt diff`

- Land a change in a local branch or on a review request:

`rbt land `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Patch your tree with a change on a review request:

`rbt patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">review_request_id</span>

- Set up RBTool to talk to a repository:

`rbt setup-repo`
