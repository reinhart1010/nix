---
layout: page
title: common/goreload (English)
description: "Live reload utility for Go programs."
content_hash: 750f798ca3cb8ee1ba22ecd11b9b0dca9f7adf68
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# goreload

Live reload utility for Go programs.
More information: <https://github.com/acoshift/goreload>.

- Watch a binary file (defaults to `.goreload`):

`goreload -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Set a custom log prefix (defaults to `goreload`):

`goreload --logPrefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.go</span>

- Reload whenever any file changes:

`goreload --all`
