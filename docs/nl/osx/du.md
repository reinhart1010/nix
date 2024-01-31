---
layout: page
title: osx/du (Nederlands)
description: "Disk gebruik: schat en groepeer bestand en map ruimte gebruik."
content_hash: 237c55ce368310b91bf0a21e95e6274f8d257aa6
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/osx/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Disk gebruik: schat en groepeer bestand en map ruimte gebruik.
Meer informatie: <https://keith.github.io/xcode-man-pages/du.1.html>.

- Toont de grootte van een map en mogelijke sub-mappen, met een gegeven eenheid (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte van een map en mogelijke sub-mappen, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte van een enkele map met een leesbaar eenheid formaat:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van een map met alle bestanden en mappen:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van een map en alle sub-mappen tot N niveaus diep:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-mappen van de huidige map en laat een cumulatief totaal zien op het eind:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
