---
layout: page
title: common/tokei (English)
description: "A program that prints out statistics about code."
content_hash: dad4672b19d7a407de8840a7503f78fda200e7ef
---
# tokei

A program that prints out statistics about code.
More information: <https://github.com/XAMPPRocky/tokei>.

- Get a report on the code in a directory and all subdirectories:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Get a report for a directory excluding `.min.js` files:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.min.js</span>

- Print out statistics for individual files in a directory:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --files`

- Get a report for all files of type Rust and Markdown:

`tokei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -t=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rust</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Markdown</span>
