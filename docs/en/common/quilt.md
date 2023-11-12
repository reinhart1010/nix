---
layout: page
title: common/quilt (English)
description: "Tool to manage a series of patches."
content_hash: 126faff45a27fdcac44fa85fc73dbe5c5790d576
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# quilt

Tool to manage a series of patches.
More information: <https://savannah.nongnu.org/projects/quilt>.

- Import an existing patch from a file:

`quilt import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.patch</span>

- Create a new patch:

`quilt new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.patch</span>

- Add a file to the current patch:

`quilt add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- After editing the file, refresh the current patch with the changes:

`quilt refresh`

- Apply all the patches in the series file:

`quilt push -a`

- Remove all applied patches:

`quilt pop -a`
