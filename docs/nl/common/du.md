---
layout: page
title: common/du (Nederlands)
description: "Disk gebruik: schat en groepeer bestand en directory ruimte gebruik."
content_hash: 24d5a8d10761dd2e52723c2110fd20d16d6bb1af
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
---
# du

Disk gebruik: schat en groepeer bestand en directory ruimte gebruik.
Meer informatie: <https://www.gnu.org/software/coreutils/du>.

- Toont de grootte van een directory en mogelijke sub-directories, met een gegeven eenheid (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte van een directory en mogelijke sub-directories, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte van een enkele directory met een leesbaar eenheid formaat:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van een directory met alle bestanden en directories:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van een directory en alle sub-directories tot N niveaus diep:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-directories van de huidige directory en laat een cumulatief totaal zien op het eind:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
