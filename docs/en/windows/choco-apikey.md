---
layout: page
title: windows/choco-apikey (English)
description: "Manage API keys for Chocolatey sources."
content_hash: 5d5d3d32dc648eba99e27ab9fbd842717545050c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco apikey

Manage API keys for Chocolatey sources.
More information: <https://chocolatey.org/docs/commands-apikey>.

- Display a list of sources and their API keys:

`choco apikey`

- Display a specific source and its API key:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url</span>`"`

- Set an API key for a source:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key</span>`"`

- Remove an API key for a source:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url</span>`" --remove`
