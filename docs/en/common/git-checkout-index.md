---
layout: page
title: common/git-checkout-index (English)
description: "Copy files from the index to the working tree."
content_hash: 81ec9175f125f9d9e2b9bfb36eaddbced7a0687b
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
