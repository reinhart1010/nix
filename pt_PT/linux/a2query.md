---
layout: page
title: linux/a2query (português (Portugal))
description: "Mostra configurações runtime do Apache em distribuições baseadas em Debian."
content_hash: ca6ed84aed976b757cb8aa82bbce8cda137047da
related_topics:
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
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
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Mostra configurações runtime do Apache em distribuições baseadas em Debian.
Mais informações: <https://manpages.debian.org/latest/apache2/a2query.html>.

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
