---
layout: page
title: common/install-nodeversion (Nederlands)
description: "Installeer Node.js runtime versies voor `ps-nvm`."
content_hash: c7240518d4fcf06f07d5a127e2e3cd06dfeae555
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/install-nodeversion.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Install-NodeVersion

Installeer Node.js runtime versies voor `ps-nvm`.
Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Installeer een specifieke Node.js versie:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Installeer meerdere Node.js versies:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie1 , node_versie2 , ...</span>

- Installeer de laatst beschikbare versie van Node.js 20:

`Install-NodeVersion ^20`

- Installeer de x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) versie van Node.js:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>` -Architecture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86|x64|arm64</span>

- Gebruik een HTTP proxy voor het downloaden van Node.js:

`Install-NodeVersion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node-version</span>` -Proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
