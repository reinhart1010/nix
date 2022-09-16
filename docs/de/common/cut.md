---
layout: page
title: common/cut (Deutsch)
description: "Schneide Felder von stdin oder einer Datei aus."
content_hash: c693622b455487bf8b19225028c36da2fb187f83
related_topics:
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cut.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cut

Schneide Felder von stdin oder einer Datei aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/cut>.

- Schneide bestimmte Zeichen oder einen Feldbereich jeder Zeile aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` | cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|fields</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Schneide einen bestimmten Bereich jeder Zeile mit einem bestimmten Trennzeichen aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` | cut --delimiter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`"`

- Schneide einen bestimmten Bereich jeder Zeile einer bestimmten Datei aus:

`cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
