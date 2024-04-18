---
layout: page
title: osx/setfile (English)
description: "Set file attributes on files in an HFS+ directory."
content_hash: 1616a08b44b492b5efe58c12b99ff461be887523
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# setfile

Set file attributes on files in an HFS+ directory.
More information: <https://ss64.com/osx/setfile.html>.

- Set creation date for specific files:

`setfile -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set modification date for specific files:

`setfile -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set modification date for symlink file (not to linked file itself):

`setfile -P -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
