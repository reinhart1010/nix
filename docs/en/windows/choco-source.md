---
layout: page
title: windows/choco-source (English)
description: "Manage sources for packages with Chocolatey."
content_hash: 301ef4d6dc70efc97619a0faaf274a3df29a2b24
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-source.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-source.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-source.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-source.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-source.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-source.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco source

Manage sources for packages with Chocolatey.
More information: <https://chocolatey.org/docs/commands-source>.

- List currently available sources:

`choco source list`

- Add a new package source:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Add a new package source with credentials:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Add a new package source with a client certificate:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\certificate_file</span>

- Enable a package source:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Disable a package source:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Remove a package source:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
