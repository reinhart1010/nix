---
layout: page
title: common/rdfind (English)
description: "Find files with duplicate content and get rid of them."
content_hash: b048a07f95034abca4d476a27a17f940687c5e2b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rdfind

Find files with duplicate content and get rid of them.
More information: <https://rdfind.pauldreik.se>.

- Identify all duplicates in a given directory and output a summary:

`rdfind -dryrun true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Replace all duplicates with hardlinks:

`rdfind -makehardlinks true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Replace all duplicates with symlinks/soft links:

`rdfind -makesymlinks true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Delete all duplicates and do not ignore empty files:

`rdfind -deleteduplicates true -ignoreempty false `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
