---
layout: page
title: common/ctags (English)
description: "Generates an index (or tag) file of language objects found in source files for many popular programming languages."
content_hash: e59f4436b3e46e037a210443e1726ff7c8a2fedc
---
# ctags

Generates an index (or tag) file of language objects found in source files for many popular programming languages.
More information: <https://ctags.io/>.

- Generate tags for a single file, and output them to a file named "tags" in the current directory, overwriting the file if it exists:

`ctags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Generate tags for all files in the current directory, and output them to a specific file, overwriting the file if it exists:

`ctags -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` *`

- Generate tags for all files in the current directory and all subdirectories:

`ctags --recurse`
