---
layout: page
title: osx/pkgutil (English)
description: "Query and manipulate Mac OS X Installer packages and receipts."
content_hash: 9818ba6e8dbc314c22d38038c72155063ec77d9a
---
# pkgutil

Query and manipulate Mac OS X Installer packages and receipts.

- List package IDs for all installed packages:

`pkgutil --pkgs`

- Verify cryptographic signatures of a package file:

`pkgutil --check-signature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.pkg</span>

- List all the files for an installed package given its ID:

`pkgutil --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.microsoft.Word</span>

- Extract the contents of a package file into a directory:

`pkgutil --expand-full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/filename.pkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
