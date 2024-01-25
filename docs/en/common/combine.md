---
layout: page
title: common/combine (English)
description: "Perform set operations on lines of two files."
content_hash: de9a81e92399d6e96a126c651d6aadff78c39258
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# combine

Perform set operations on lines of two files.
The order of the output lines is determined by the order of the lines in the first file.
See also: `diff`.
More information: <https://joeyh.name/code/moreutils/>.

- Output lines that are in both specified files:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` and `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Output lines that are in the first but not in the second file:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` not `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Output lines that in are in either of the specified files:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` or `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Output lines that are in exactly one of the specified files:

`combine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` xor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
