---
layout: page
title: common/goreload (English)
description: "Live reload utility for Go programs."
content_hash: c3a670b8054f603b8f939c45a6b75532e36a2752
---
# goreload

Live reload utility for Go programs.
More information: <https://github.com/acoshift/goreload>.

- Set the name of the binary file to watch (defaults to `.goreload`):

`goreload -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- Set a custom log prefix (defaults to `goreload`):

`goreload --logPrefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- Reload whenever any file changes:

`goreload --all`
