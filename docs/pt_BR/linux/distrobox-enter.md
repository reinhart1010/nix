---
layout: page
title: linux/distrobox-enter (português (Brasil))
description: "Entrar em um contêiner distrobox. Veja também: `tldr distrobox`."
content_hash: 6a7df205125b691856c3bd4c55b7752b673e21fe
last_modified_at: 2023-11-20
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

Entrar em um contêiner distrobox. Veja também: `tldr distrobox`.
O comando padrão executado é o seu SHELL, mas você pode especificar shells diferentes ou comandos completos para serem executados.
Se usado dentro de um script, um aplicativo ou um serviço, você pode usar o modo `--headless` para desabilitar o tty e a interatividade.
Mais informações: <https://distrobox.it/usage/distrobox-enter>.

- Entrar em um contêiner distrobox:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Entrar em um contêiner distrobox e executar um comando no login:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Entrar em um contêiner distrobox sem instanciar um tty:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
