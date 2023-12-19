---
layout: page
title: common/winicontopam (Nederlands)
description: "Converteer een Windows ICO bestand naar een PAM bestand."
content_hash: 9984fe82399dc922f7752650f603b28afde8c393
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/winicontopam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# winicontopam

Converteer een Windows ICO bestand naar een PAM bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/winicontopam.html>.

- Lees een ICO bestand en converteer de beste kwaliteit afbeelding daarin naar het PAM formaat:

`winicontopam `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Converteer alle afbeeldingen in het invoerbestand naar PAM:

`winicontopam -allimages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Converteer de n afbeelding in het invoerbestand naar PAM:

`winicontopam -image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Als de afbeelding(en) voor te extraheren bevatten transparantie data en een AND mask, scrhijf de AND mask naar het vijfde kanaal van het uitvoer PAM bestand:

`winicontopam -andmasks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.ico</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
