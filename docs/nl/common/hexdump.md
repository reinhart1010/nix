---
layout: page
title: common/hexdump (Nederlands)
description: "Een ASCII, decimaal, hexadecimale, octale dump."
content_hash: eedc0fb3ae8b8077695cee3d43cda5407b486fd6
last_modified_at: 2023-11-07
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># hexdump

Een ASCII, decimaal, hexadecimale, octale dump.
Meer informatie: <https://manned.org/hexdump>.

- Toon de hexadecimale weergave van een bestand en vervang dubbele regels door '*':

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de invoeroffset in hexadecimaal en zijn ASCII-weergave in twee kolommen:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef de hexadecimale weergave van een bestand weer, maar interpreteer alleen n bytes van de invoer:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal_bytes</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang geen dubbele regels door '*':

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
