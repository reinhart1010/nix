---
layout: page
title: common/errno (español)
description: "Busca nombres y descripciones erróneos."
content_hash: 5af18f33b2c499009059a22edd12afd09405da53
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/errno.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/errno.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/errno.html
    icon: bi bi-globe
tldri18n_status: 2
---
# errno

Busca nombres y descripciones erróneos.
Más información: <https://joeyh.name/code/moreutils/>.

- Busca descripción errno por nombre o código:

`errno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|code</span>

- Lista todos los nombres errno, códigos y descripciones:

`errno --list`

- Busca código cuya descripción contiene todo el texto dado:

`errno --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>

- Busca código cuya descripción contiene todo el texto dado (en todos los locales):

`errno --search-all-locales `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>
