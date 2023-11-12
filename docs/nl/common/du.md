---
layout: page
title: common/du (Nederlands)
description: "Disk gebruik: schat en groepeer bestand en map ruimte gebruik."
content_hash: cd9f7aff181ab41c5a66559c8fb6a825b28c14ac
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Disk gebruik: schat en groepeer bestand en map ruimte gebruik.
Meer informatie: <https://www.gnu.org/software/coreutils/du>.

- Toont de grootte van een map en mogelijke sub-mappen, met een gegeven eenheid (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte van een map en mogelijke sub-mappen, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte van een enkele map met een leesbaar eenheid formaat:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van een map met alle bestanden en mappen:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van een map en alle sub-mappen tot N niveaus diep:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-mappen van de huidige map en laat een cumulatief totaal zien op het eind:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
