---
layout: page
title: common/cut (español)
description: "Corta campos de `stdin` o archivos."
content_hash: 006f5f163a442e0676100c9411934a3240fe3477
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cut

Corta campos de `stdin` o archivos.
Más información: <https://www.gnu.org/software/coreutils/cut>.

- Imprime un rango específico de caracteres/campos de cada línea:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">characters|field</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|1,10|1-10|1-|-10</span>

- Imprime un rango de cada línea con un delimitador específico:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | cut --delimiter="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>`" --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">campos</span>`={1</span>

- Imprime un rango de cada línea de un archivo específico:

`cut --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caracteres</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
