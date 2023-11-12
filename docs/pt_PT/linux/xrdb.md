---
layout: page
title: linux/xrdb (português (Portugal))
description: "Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix."
content_hash: 95cd1d484d0c417e06436d80773c776f20e6ff2d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xrdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrdb

Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix.
Mais informações: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Iniciar `xrdb` em modo interactivo:

`xrdb`

- Carregar valores (p. ex. regras de estilo) de um ficheiro de recursos:

`xrdb -load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.Xresources</span>

- Consultar base de dados de recursos e mostrar estado actual dos recursos:

`xrdb -query`
