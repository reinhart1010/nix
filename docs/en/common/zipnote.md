---
layout: page
title: common/zipnote (English)
description: "View, add, or edit a Zip archive's comments."
content_hash: ef8a9d2da97f6f181f2a842f01aec0a445ed95e6
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# zipnote

View, add, or edit a Zip archive's comments.
Files can also be renamed in the Zip archive.
More information: <https://manned.org/zipnote>.

- View the comments on a Zip archive:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Extract the comments on a Zip archive to a file:

`zipnote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Add/Update comments in a Zip archive from a file:

`zipnote -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>
