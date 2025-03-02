---
layout: page
title: linux/df (Nederlands)
description: "Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte."
content_hash: dc5f41d6749630f3ec7c31ec87ee4b1c7b194dd4
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

Toon een overzicht van het gebruik van het bestandssysteem op het gebied van schijfruimte.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>.

- Toon alle bestandssystemen en hun schijfgebruik:

`df`

- Toon alle bestandssystemen en hun schijfgebruik in een leesbaar formaat:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--human-readable</span>

- Toon het bestandssysteem en het schijfgebruik voor het opgegeven bestand of map:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Neem statistieken op over het aantal beschikbare inodes:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--inodes</span>

- Toon bestandssystemen maar negeer specifieke types:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

- Toon bestandssysteem-types:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--print-type</span>
