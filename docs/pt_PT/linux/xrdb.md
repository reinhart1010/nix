---
layout: page
title: linux/xrdb (português (Portugal))
description: "Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix."
content_hash: 81bb44f1ccbbac43c1e2427b5d0324d55b2f128a
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/xrdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrdb

Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix.
Mais informações: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Inicia `xrdb` em modo interactivo:

`xrdb`

- Carrega valores (p. ex. regras de estilo) de um ficheiro de recursos:

`xrdb -load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.Xresources</span>

- Consulta base de dados de recursos e mostra estado actual dos recursos:

`xrdb -query`
