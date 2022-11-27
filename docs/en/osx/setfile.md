---
layout: page
title: osx/setfile (English)
description: "Sets file attributes on files in an HFS+ directory."
content_hash: a198b0a19868d80560b35ce2cb48a74e8408667f
last_modified_at: 2022-11-27
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># setfile

Sets file attributes on files in an HFS+ directory.
More information: <https://ss64.com/osx/setfile.html>.

- Set creation date for specific files:

`setfile -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set modification date for specific files:

`setfile -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Set modification date for symlink file (not to linked file itself):

`setfile -P -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MM/DD/YYYY HH:MM:SS</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
