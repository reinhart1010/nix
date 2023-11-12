---
layout: page
title: windows/choco-new (English)
description: "Generate new package specification files with Chocolatey."
content_hash: 8266c55787db4001d563c8a28a4ecc0261b9f938
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-new.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-new.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-new.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-new.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-new.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco new

Generate new package specification files with Chocolatey.
More information: <https://chocolatey.org/docs/commands-new>.

- Create a new package skeleton:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Create a new package with a specific version:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Create a new package with a specific maintainer name:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --maintainer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maintainer_name</span>

- Create a new package in a custom output directory:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a new package with specific 32-bit and 64-bit installer URLs:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` url="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`" url64="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
