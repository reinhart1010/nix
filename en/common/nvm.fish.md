---
layout: page
title: common/nvm.fish (English)
description: "Install, uninstall, or switch between Node.js versions under the `fish` shell."
content_hash: 020432b4f994089ff33d5cd953c4064f6031eb5a
---
# nvm

Install, uninstall, or switch between Node.js versions under the `fish` shell.
Supports version numbers like "12.8" or "v16.13.1", and labels like "stable", "system", etc.
More information: <https://github.com/jorgebucaran/nvm.fish>.

- Install a specific version of Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Use a specific version of Node.js in the current shell:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Set the default Node.js version:

`set nvm_default_version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- List all available Node.js versions and highlight the default one:

`nvm list`

- Uninstall a given Node.js version:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>
