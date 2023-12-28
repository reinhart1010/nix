---
layout: page
title: linux/distrobox-create (português (Brasil))
description: "Criar um contêiner Distrobox. Veja também: `tldr distrobox`."
content_hash: e9140c7c2b26beb2908fcd109eeef5ac5bb3f0d1
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-create

Criar um contêiner Distrobox. Veja também: `tldr distrobox`.
O contêiner criado será integrado ao sistema host, permitindo o compartilhamento do diretório HOME do usuário, armazenamento externo, dispositivos USB externos, aplicativos gráficos (X11/Wayland) e áudio.
Mais informações: <https://distrobox.it/usage/distrobox-create>.

- Cria um contêiner Distrobox usando a imagem do Ubuntu:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Clona um contêiner Distrobox:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner_clonado</span>
