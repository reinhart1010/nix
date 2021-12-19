---
layout: page
title: osx/du (Nederlands)
description: "Disk gebruik: schat en groepeer bestand en directory ruimte gebruik."
content_hash: 4413b8beece9724196855c9ce2f98a61287d1a18
related_topics:
  - title: English version
    url: /en/osx/du.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/du.html
    icon: bi bi-globe
---
# du

Disk gebruik: schat en groepeer bestand en directory ruimte gebruik.
Meer informatie: <https://ss64.com/osx/du.html>.

- Toont de grootte van een directory en mogelijke sub-directories, met een gegeven eenheid (KiB/MiB/GiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte van een directory en mogelijke sub-directories, met een leesbaar unit formaat (bijvoorbeeld door het automatisch kiezen van een eenheid gebaseerd op grootte)):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte van een enkele directory met een leesbaar eenheid formaat:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van een directory met alle bestanden en directories:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van een directory en alle sub-directories tot N niveaus diep:

`du -h -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Toont de grootte in leesbare vorm van alle `.jpg` bestanden in sub-directories van de huidige directory en laat een cumulatief totaal zien op het eind:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
