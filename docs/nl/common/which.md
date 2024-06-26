---
layout: page
title: common/which (Nederlands)
description: "Zoek een programma in het pad van de gebruiker."
content_hash: 33e703d0fafeefd6e778598f1d653d086ed6851c
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/common/which.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/which.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/which.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/which.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/which.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/which.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># which

Zoek een programma in het pad van de gebruiker.
Meer informatie: <https://manned.org/which>.

- Doorzoek de PATH-omgevingsvariabele en toon de locatie van eventuele overeenkomende uitvoerbare bestanden:

`which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>

- Als er meerdere uitvoerbare bestanden zijn die overeenkomen, toon ze allemaal:

`which -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>
