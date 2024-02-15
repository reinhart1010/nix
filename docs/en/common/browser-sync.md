---
layout: page
title: common/browser-sync (English)
description: "A local web server that updates browser on file changes."
content_hash: cbf5cea98bb8887146e08d8446d83e8c38086277
last_modified_at: 2024-02-15
related_topics:
  - title: italiano version
    url: /it/common/browser-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/browser-sync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/browser-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# browser-sync

A local web server that updates browser on file changes.
More information: <https://browsersync.io/docs/command-line>.

- Start a server from a specific directory:

`browser-sync start --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start a server from local directory, watching all CSS files in a directory:

`browser-sync start --server --files '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/*.css</span>`'`

- Create configuration file:

`browser-sync init`

- Start Browsersync from configuration file:

`browser-sync start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file</span>
