---
layout: page
title: common/npm (Nederlands)
description: "JavaScript en Node.js pakketbeheerder."
content_hash: c23fe5aaaeadcfbb8b305dbb8d7786b2b1687955
last_modified_at: 2024-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

JavaScript en Node.js pakketbeheerder.
Beheer Node.js-projecten en hun module-afhankelijkheden.
Meer informatie: <https://www.npmjs.com>.

- Maak een `package.json`-bestand met standaardwaarden (laat --yes weg om dit interactief te doen):

`npm init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--yes</span>

- Download alle pakketten die zijn vermeld als afhankelijkheden in `package.json`:

`npm install`

- Download een specifieke versie van een pakket en voeg het toe aan de lijst van afhankelijkheden in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>

- Download de nieuwste versie van een pakket en voeg het toe aan de lijst van dev-afhankelijkheden in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Download de nieuwste versie van een pakket en installeer het globaal:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>

- Verwijder een pakket en haal het uit de lijst van afhankelijkheden in `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>

- Toon alle lokaal geïnstalleerde afhankelijkheden:

`npm list`

- Toon alle top-level globaal geïnstalleerde pakketten:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
