---
layout: page
title: linux/a2query (português (Portugal))
description: "Mostra configurações runtime do Apache em distribuições baseadas em Debian."
content_hash: 241744f6c606be764449ffa484d386c9d93d4dd4
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2query

Mostra configurações runtime do Apache em distribuições baseadas em Debian.
Mais informações: <https://manned.org/a2query>.

- Lista módulos Apache activados:

`sudo a2query -m`

- Verifica de um módulo específico está instalado:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Lista os hosts virtuais activados:

`sudo a2query -s`

- Mostra o módulo de multi processamento actualmente activado:

`sudo a2query -M`

- Mostra a versão do Apache:

`sudo a2query -v`
