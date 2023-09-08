---
layout: page
title: linux/distrobox-create (português (Brasil))
description: "Criar um contêiner distrobox. Veja também: `tldr distrobox`."
content_hash: 6a7a1c2f1d2a10da9a519bc791b09a9e6731c530
last_modified_at: 2023-09-08
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-create

Criar um contêiner distrobox. Veja também: `tldr distrobox`.
O contêiner criado será integrado ao sistema host, permitindo o compartilhamento do diretório HOME do usuário, armazenamento externo, dispositivos USB externos, aplicativos gráficos (X11/Wayland) e áudio.
Mais informações: <https://distrobox.privatedns.org/usage/distrobox-create.html>.

- Criar um contêiner distrobox usando a imagem do Ubuntu:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Clonar um contêiner distrobox:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner_clonado</span>
