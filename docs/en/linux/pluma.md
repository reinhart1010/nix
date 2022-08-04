---
layout: page
title: linux/pluma (English)
description: "Edit files in MATE desktop environment."
content_hash: b0fd701733ea64a0b76dedd7e5c5a37ce4cc9517
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pluma

Edit files in MATE desktop environment.
More information: <https://manned.org/pluma>.

- Start the editor:

`pluma`

- Open specific documents:

`pluma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Open documents using a specific encoding:

`pluma --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WINDOWS-1252</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print all supported encodings:

`pluma --list-encodings`

- Open document and go to a specific line:

`pluma +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
