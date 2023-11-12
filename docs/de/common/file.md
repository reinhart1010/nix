---
layout: page
title: common/file (Deutsch)
description: "Bestimmen des Dateityps."
content_hash: 471ca203b4030f1772989a87a027ab16a43a26af
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# file

Bestimmen des Dateityps.
Weitere Informationen: <https://manned.org/file>.

- Gibt eine Beschreibung des Typs der angegebenen Datei zurück. Funktioniert bei Dateien ohne Dateiendung:

`file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Bestimmt die Dateityp(en) in einer gezippten Datei:

`file -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiv.zip</span>

- Zulassen, dass die Datei mit speziellen oder Gerätedateien arbeitet:

`file -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Hört nicht bei der ersten Dateityp-Übereinstimmung auf; weitermachen bis zum Ende der Datei:

`file -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Bestimmen des MIME-Codierungstyp einer Datei:

`file -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>
