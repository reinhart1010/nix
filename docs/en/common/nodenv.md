---
layout: page
title: common/nodenv (English)
description: "A tool to manage Node.js versions."
content_hash: 653caedf73ce9364b1e25b3043e094480b5891c6
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/nodenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nodenv

A tool to manage Node.js versions.
More information: <https://github.com/nodenv/nodenv>.

- Install a specific version of Node.js:

`nodenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display a list of available versions:

`nodenv install --list`

- Use a specific version of Node.js across the whole system:

`nodenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Use a specific version of Node.js with a directory:

`nodenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Display the Node.js version for the current directory:

`nodenv version`

- Display the location of a Node.js installed command (e.g. `npm`):

`nodenv which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
