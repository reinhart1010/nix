---
layout: page
title: common/git-checkout-index (English)
description: "Copy files from the index to the working tree."
content_hash: 81ec9175f125f9d9e2b9bfb36eaddbced7a0687b
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-checkout-index.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout-index

Copy files from the index to the working tree.
More information: <https://git-scm.com/docs/git-checkout-index>.

- Restore any files deleted since the last commit:

`git checkout-index --all`

- Restore any files deleted or changed since the last commit:

`git checkout-index --all --force`

- Restore any files changed since the last commit, ignoring any files that were deleted:

`git checkout-index --all --force --no-create`

- Export a copy of the entire tree at the last commit to the specified directory (the trailing slash is important):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/export_directory/</span>
