---
layout: page
title: windows/cmd (Nederlands)
description: "De Windows-opdrachtinterpreter."
content_hash: 4c5579af77d8198cd27dbba462fc0a67b60cf804
last_modified_at: 2024-08-13
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/cmd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmd

De Windows-opdrachtinterpreter.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Start een interactieve shell-sessie:

`cmd`

- Voer specifieke [c]ommandos uit:

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>

- Voer een specifiek script uit:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\script.bat</span>

- Voer specifieke commando's uit en start vervolgens een interactieve shell:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>

- Start een interactieve shell-sessie waarbij `echo` is uitgeschakeld in de opdrachtuitvoer:

`cmd /q`

- Start een interactieve shell-sessie met vertraagde [v]ariabele-expansie in- of uitgeschakeld:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Start een interactieve shell-sessie met opdracht[e]xtensies in- of uitgeschakeld:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Start een interactieve shell-sessie met gebruikte [u]nicode-codering:

`cmd /u`
