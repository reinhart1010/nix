---
layout: page
title: common/trans (español)
description: "Translate Shell es un traductor de línea de comandos."
content_hash: 754740eaa89a66eb23a2b616ee4957a3c3338acf
last_modified_at: 2025-01-05
related_topics:
  - title: English version
    url: /en/common/trans.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/trans.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trans

Translate Shell es un traductor de línea de comandos.
Más información: <https://github.com/soimort/translate-shell>.

- Traduce una palabra (el idioma es detectado automáticamente):

`trans "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_u_oración_a_traducir</span>`"`

- Genera una traducción corta:

`trans --brief "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_u_oración_a_traducir</span>`"`

- Traduce una palabra al español:

`trans :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">es</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra</span>

- Traduce una palabra del alemán al español:

`trans `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">es</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Schmetterling</span>

- Se comporta como un diccionario para obtener el significado de una palabra:

`trans -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra</span>
