---
layout: page
title: common/rc (English)
description: "A modern simplistic port listener & reverse shell."
content_hash: 28011d849c7304d0182ec434c6783fba8342d64c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rc

A modern simplistic port listener & reverse shell.
Similar to `nc`.
More information: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Start listening on a specific port:

`rc -lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start a reverse shell:

`rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell</span>
