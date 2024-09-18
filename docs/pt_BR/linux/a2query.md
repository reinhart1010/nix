---
layout: page
title: linux/a2query (português (Brasil))
description: "Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian."
content_hash: f7d96ce3162df5236ab2ac3377d4622b11dabc68
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
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
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

Exibe configurações de execução do Apache em sistemas operacionais baseados no Debian.
Mais informações: <https://manned.org/a2query>.

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
