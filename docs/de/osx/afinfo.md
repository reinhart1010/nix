---
layout: page
title: osx/afinfo (Deutsch)
description: "Audiodatei-Metadaten-Parser für OS X."
content_hash: 0f588fa8cd10b5fb968ac40890fb1120f03f9997
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/osx/afinfo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/afinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/afinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># afinfo

Audiodatei-Metadaten-Parser für OS X.
Eingebauter Befehl von OS X.
Weitere Informationen: <https://keith.github.io/xcode-man-pages/afinfo.1.html>.

- Zeige Informationen zu einer bestimmten Audiodatei an:

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib eine einzeilige Beschreibung der Audiodatei aus:

`afinfo --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib Metadaten und den Inhalt des InfoDictionary der Audiodatei aus:

`afinfo --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib die Daten im XML-Format aus:

`afinfo --xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Gib Warnungen für die Audiodatei aus, falls vorhanden:

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Zeige eine Hilfe an:

`afinfo --help`
