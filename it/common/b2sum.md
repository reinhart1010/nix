---
layout: page
title: common/b2sum (italiano)
description: "Calcola checksum BLAKE2."
content_hash: 8fa1192d246f04e09f45c95cec703b087f33ac2f
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
---
# b2sum

Calcola checksum BLAKE2.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/b2sum>.

- Calcola il checksum BLAKE2 per un file:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>

- Calcola checksum BLAKE2 per più file:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Leggi un file di checksum BLAKE2 e nomi di file e verifica che tutti i file abbiano lo stesso checksum:

`b2sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">elenco_checksum.b2</span>

- Calcola il checksum BLAKE2 da standard input:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | b2sum`
