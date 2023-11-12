---
layout: page
title: windows/choco-pin (English)
description: "Pin a package at a specific version with Chocolatey."
content_hash: 7b34dfe48db72ae801a01ed3680f686bda427d85
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-pin.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-pin.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-pin.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-pin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco pin

Pin a package at a specific version with Chocolatey.
Pinned packages are skipped automatically when upgrading.
More information: <https://chocolatey.org/docs/commands-pin>.

- Display a list of pinned packages and their versions:

`choco pin list`

- Pin a package at its current version:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Pin a package at a specific version:

`choco pin add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Remove a pin for a specific package:

`choco pin remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
