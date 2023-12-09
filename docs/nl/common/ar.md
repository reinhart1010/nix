---
layout: page
title: common/ar (Nederlands)
description: "Maken, aanpassen en uitpakken van Unix archieven. Typisch gebruikt voor statische bibliotheken (`.a`) en Debian pakketten (`.deb`)."
content_hash: fb8a36e8e4fc3386e6a2d49079f8eed44ba21bb1
last_modified_at: 2023-12-09
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ar

Maken, aanpassen en uitpakken van Unix archieven. Typisch gebruikt voor statische bibliotheken (`.a`) en Debian pakketten (`.deb`).
Bekijk ook: `tar`.
Meer informatie: <https://manned.org/ar>.

- Pak alles uit van een archief:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.a</span>

- [t]oon inhoud van een specifiek archief:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.ar</span>

- Ve[r]vang of voeg specifieke bestanden toe aan een archief:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/debian-binary pad/naar/control.tar.gz pad/naar/data.tar.xz ...</span>

- Voeg een object bestandsindex toe (equivalent aan het gebruik van `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.a</span>

- Maak een archief met specifieke bestanden en een begeleidend object bestandsindex:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1.o pad/naar/bestand2.o ...</span>
