---
layout: page
title: common/install-nodeversion (English)
description: "Install Node.js runtime versions for `ps-nvm`."
content_hash: f76e85b623396bbb3f44a0a49b3c2c631b343501
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Install-NodeVersion

Install Node.js runtime versions for `ps-nvm`.
This command is part of `ps-nvm` and can only be run under PowerShell.
More information: <https://github.com/aaronpowell/ps-nvm>.

- Install a specific Node.js version:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Install multiple Node.js versions:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version1 , node_version2 , ...</span>

- Install latest available version of Node.js 20:

`Install-NodeVersion ^20`

- Install the x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) version of Node.js:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` -Architecture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86|x64|arm64</span>

- Use a HTTP proxy to download Node.js:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node-version</span>` -Proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
