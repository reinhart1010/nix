---
layout: page
title: common/export (Deutsch)
description: "Befehl zum Markieren von Shell-Variablen in der aktuellen Umgebung, die mit allen neu abgezweigten Unterprozessen exportiert werden sollen."
content_hash: b5a0a4ae316dc8ec9084479335e3881ba3f26019
last_modified_at: 2024-01-09
related_topics:
  - title: English version
    url: /en/common/export.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/export.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/export.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># export

Befehl zum Markieren von Shell-Variablen in der aktuellen Umgebung, die mit allen neu abgezweigten Unterprozessen exportiert werden sollen.
Weitere Informationen: <https://manned.org/export.1posix>.

- Lege eine neue Umgebungsvariable fest:

`export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert</span>

- Entferne eine Umgebungsvariable:

`export -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>

- Markiere eine Shell-Funktion für den Export:

`export -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funktionsname</span>

- Hänge etwas an die PATH-Variable an:

`export PATH=$PATH:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/anhängen</span>
