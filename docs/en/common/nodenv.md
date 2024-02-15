---
layout: page
title: common/nodenv (English)
description: "Manage Node.js versions."
content_hash: 1cffbe4c4397a5d3b46bdc2c62fbee5aa6752525
last_modified_at: 2024-02-15
related_topics:
  - title: Deutsch version
    url: /de/common/nodenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nodenv

Manage Node.js versions.
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
