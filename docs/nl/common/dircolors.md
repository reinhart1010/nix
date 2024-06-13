---
layout: page
title: common/dircolors (Nederlands)
description: "Geef commando's weer om de LS_COLOR-omgevingsvariabele in te stellen en style `ls`, `dir` enz."
content_hash: 0f4599638bd749709e1fee2708520bb99343f35d
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/dircolors.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dircolors.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dircolors

Geef commando's weer om de LS_COLOR-omgevingsvariabele in te stellen en style `ls`, `dir` enz.
Meer informatie: <https://www.gnu.org/software/coreutils/dircolors>.

- Geef commando's weer om LS_COLOR in te stellen met standaardkleuren:

`dircolors`

- Geef commando's weer om LS_COLOR in te stellen met kleuren uit een bestand:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef commando's weer voor de Bourne-shell:

`dircolors --bourne-shell`

- Geef commando's weer voor de C-shell:

`dircolors --c-shell`

- Bekijk de standaardkleuren voor bestandstypen en extensies:

`dircolors --print-data`
