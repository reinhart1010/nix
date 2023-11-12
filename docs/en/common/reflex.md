---
layout: page
title: common/reflex (English)
description: "Tool to watch a directory and rerun a command when certain files change."
content_hash: 00d25f74b9a8a6bc3570a524051aa450990d2af3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# reflex

Tool to watch a directory and rerun a command when certain files change.
More information: <https://github.com/cespare/reflex>.

- Rebuild with `make` if any file changes:

`reflex make`

- Compile and run Go application if any `.go` file changes:

`reflex --regex='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\.go$</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go run .</span>

- Ignore a directory when watching for changes:

`reflex --inverse-regex='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^dir/</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Run command when reflex starts and restarts on file changes:

`reflex --start-service=true `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Substitute the filename that changed in:

`reflex -- echo {}`
