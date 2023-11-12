---
layout: page
title: common/pdftotext (Deutsch)
description: "Konvertiere PDF Dateien zum plain text Format."
content_hash: 40055bfa884b6cfdab0bf99ce431fb4de5db615d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pdftotext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftotext

Konvertiere PDF Dateien zum plain text Format.
Weitere Informationen: <https://www.xpdfreader.com/pdftotext-man.html>.

- Konvertiere `datei.pdf` zu plain text und gib sie über die Standardausgabe aus:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.pdf</span>` -`

- Konvertiere `datei.pdf` zu plain text und speichere sie als `datei.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.pdf</span>

- Konvertiere `datei.pdf` zu plain text und erhalte das Layout:

`pdftotext -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.pdf</span>

- Konvertiere `quelldatei.pdf` zu plain text und speichere sie als `zieldatei.txt`:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zieldatei.txt</span>

- Konvertiere Seite 2, 3 und 4 von `quelldatei.pdf` zu plain text und speichere sie als `zieldatei.txt`:

`pdftotext -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zieldatei.txt</span>
