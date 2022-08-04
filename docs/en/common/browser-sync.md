---
layout: page
title: common/browser-sync (English)
description: "Starts local web server that updates browser on file changes."
content_hash: f77053ad746e89a425197c15884ef27b199bc2c8
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
---
# browser-sync

Starts local web server that updates browser on file changes.
More information: <https://browsersync.io/docs/command-line>.

- Start a server from a specific directory:

`browser-sync start --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start a server from local directory, watching all CSS files in a directory:

`browser-sync start --server --files '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/*.css</span>`'`

- Create configuration file:

`browser-sync init`

- Start browser-sync from config file:

`browser-sync start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_file</span>
