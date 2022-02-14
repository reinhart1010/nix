---
layout: page
title: osx/pkgutil (English)
description: "Query and manipulate Mac OS X Installer packages and receipts."
content_hash: 4bb6e5cc9c8935fad498bd26195528ac3cf2ffe4
---
# pkgutil

Query and manipulate Mac OS X Installer packages and receipts.
More information: <https://ss64.com/osx/pkgutil.html>.

- List package IDs for all installed packages:

`pkgutil --pkgs`

- Verify cryptographic signatures of a package file:

`pkgutil --check-signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.pkg</span>

- List all the files for an installed package given its ID:

`pkgutil --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.microsoft.Word</span>

- Extract the contents of a package file into a directory:

`pkgutil --expand-full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.pkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
