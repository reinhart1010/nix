---
layout: page
title: windows/choco-source (Deutsch)
description: "Verwalte die Paketquellen mit Chocolatey."
content_hash: 5f1cb9e77a50ef9293cc8fb8ad0ddbc872b8a7ed
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/choco-source.html
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

Verwalte die Paketquellen mit Chocolatey.
Weitere Informationen: <https://chocolatey.org/docs/commands-source>.

- Gib alle momentan verfügbaren Quellen aus:

`choco source list`

- Füge eine neue Paketquelle hinzu:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Füge eine neue Paketquelle mit Zugangsdaten hinzu:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">passwort</span>

- Füge eine neue Paketquelle mit Client-Zertifikat hinzu:

`choco source add --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zertifikat</span>

- Aktiviere eine Paketquelle:

`choco source enable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Deaktiviere eine Paketquelle:

`choco source disable --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Entferne eine Paketquelle:

`choco source remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
