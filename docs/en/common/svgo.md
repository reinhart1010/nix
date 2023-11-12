---
layout: page
title: common/svgo (English)
description: "SVG Optimizer: a Node.js-based tool for optimizing Scalable Vector Graphics files."
content_hash: 7af6d3021e59147599924c78926d962ebff4ef4d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# svgo

SVG Optimizer: a Node.js-based tool for optimizing Scalable Vector Graphics files.
It applies a series of transformation rules (plugins), which can be toggled individually.
More information: <https://github.com/svg/svgo>.

- Optimize a file using the default plugins (overwrites the original file):

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test.svg</span>

- Optimize a file and save the result to another file:

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test.min.svg</span>

- Optimize all SVG files within a directory (overwrites the original files):

`svgo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/with/svg/files</span>

- Optimize all SVG files within a directory and save the resulting files to another directory:

`svgo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input/directory</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output/directory</span>

- Optimize SVG content passed from another command, and save the result to a file:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat test.svg</span>` | svgo -i - -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test.min.svg</span>

- Optimize a file and print out the result:

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test.svg</span>` -o -`

- Show available plugins:

`svgo --show-plugins`
