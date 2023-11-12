---
layout: page
title: windows/nvm (English)
description: "Install, uninstall, or switch between Node.js versions."
content_hash: 4aa57826b459c27b7572ffdb2a97800ffd970ae2
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Install, uninstall, or switch between Node.js versions.
Supports version numbers like "12.8" or "v16.13.1", and labels like "stable", "system", etc.
More information: <https://github.com/coreybutler/nvm-windows>.

- Install a specific version of Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Set the default version of Node.js (must be run as Administrator):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- List all available Node.js versions and highlight the default one:

`nvm list`

- List all remote Node.js versions:

`nvm ls-remote`

- Uninstall a given Node.js version:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>
