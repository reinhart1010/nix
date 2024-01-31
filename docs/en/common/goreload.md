---
layout: page
title: common/goreload (English)
description: "Live reload utility for Go programs."
content_hash: 310b9bcf577414c1f182a9add718092ee7be56b1
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# goreload

Live reload utility for Go programs.
More information: <https://github.com/acoshift/goreload>.

- Set the name of the binary file to watch (defaults to `.goreload`):

`goreload -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Set a custom log prefix (defaults to `goreload`):

`goreload --logPrefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Reload whenever any file changes:

`goreload --all`
