---
layout: page
title: common/zipnote (English)
description: "View, add, or edit a `zip` archive's comments."
content_hash: ff3616c0f1ad875edd19eec0c0608c56ba52cba8
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# zipnote

View, add, or edit a `zip` archive's comments.
Files can also be renamed in the `zip` archive.
More information: <https://manned.org/zipnote>.

- View the comments on a `zip` archive:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Extract the comments on a `zip` archive to a file:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Add/Update comments in a `zip` archive from a file:

`zipnote -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
