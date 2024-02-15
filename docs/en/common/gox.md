---
layout: page
title: common/gox (English)
description: "Cross-compile Go programs."
content_hash: 47423006cd53757c4ba188a885f0af67703e0d71
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# gox

Cross-compile Go programs.
More information: <https://github.com/mitchellh/gox>.

- Compile Go program in the current directory for all operating systems and architecture combinations:

`gox`

- Download and compile a Go program from a remote URL:

`gox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- Compile current directory for a particular operating system:

`gox -os="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>`"`

- Compile current directory for a single operating system and architecture combination:

`gox -osarch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>`"`
