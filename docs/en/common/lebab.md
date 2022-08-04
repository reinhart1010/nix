---
layout: page
title: common/lebab (English)
description: "A JavaScript modernizer for transpiling code to ES6/ES7."
content_hash: 551789456c56fa0c093ad6afa188e2dee763f9a6
---
# lebab

A JavaScript modernizer for transpiling code to ES6/ES7.
Transformations must be provided for all examples.
More information: <https://github.com/lebab/lebab>.

- Display a list of the available transformations:

`lebab --help`

- Transpile using one or more comma-separated transformations:

`lebab --transform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">transformation</span>

- Transpile a file to stdout:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Transpile a file to the specified output file:

`lebab `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- Replace all `.js` files in-place in the specified directory, glob or file:

`lebab --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory|glob|file</span>
