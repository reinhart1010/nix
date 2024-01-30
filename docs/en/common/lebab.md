---
layout: page
title: common/lebab (English)
description: "A JavaScript modernizer for transpiling code to ES6/ES7."
content_hash: 06029989d51eb617ad8766360207c60f229b0e37
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# lebab

A JavaScript modernizer for transpiling code to ES6/ES7.
Transformations must be provided for all examples.
More information: <https://github.com/lebab/lebab>.

- Transpile using one or more comma-separated transformations:

`lebab --transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transformation</span>

- Transpile a file to `stdout`:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Transpile a file to the specified output file:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Replace all `.js` files in-place in the specified directory, glob or file:

`lebab --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory|glob|file</span>

- Display help:

`lebab --help`
