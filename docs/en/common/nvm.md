---
layout: page
title: common/nvm (English)
description: "Install, uninstall or switch between Node.js versions."
content_hash: e0f446b8e0465630258870baa83be8f005104ea8
last_modified_at: 2024-01-09
related_topics:
  - title: Deutsch version
    url: /de/common/nvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Install, uninstall or switch between Node.js versions.
Supports version numbers like "12.8" or "v16.13.1", and labels like "stable", "system", etc.
See also: `asdf`.
More information: <https://github.com/creationix/nvm>.

- Install a specific version of Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Use a specific version of Node.js in the current shell:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Set the default Node.js version:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Launch the REPL of a specific version of Node.js:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` --version`

- Execute a script in a specific version of Node.js:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
