---
layout: page
title: linux/a2query (português (Brasil))
description: "Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian."
content_hash: 63bb9af9f794e2c921cfd039345f40c45fae1be9
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
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian.
Mais informações: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Lista módulos ativos do Apache:

`sudo a2query -m`

- Verifica se um módulo específico está instalado:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_modulo</span>

- Lista host virtuais ativos:

`sudo a2query -s`

- Exibe o módulo de multi processamento atualmente ativo:

`sudo a2query -M`

- Mostra a versão do Apache:

`sudo a2query -v`
