---
layout: page
title: linux/distrobox-enter (português (Brasil))
description: "Entrar em um contêiner Distrobox. Veja também: `tldr distrobox`."
content_hash: a5e6f97071b91261efb0d4dafd8fe902f076380a
last_modified_at: 2023-12-28
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

Entrar em um contêiner Distrobox. Veja também: `tldr distrobox`.
O comando padrão executado é o seu SHELL, mas você pode especificar shells diferentes ou comandos completos para serem executados.
Se usado dentro de um script, um aplicativo ou um serviço, você pode usar o modo `--headless` para desabilitar o tty e a interatividade.
Mais informações: <https://distrobox.it/usage/distrobox-enter>.

- Entra em um contêiner Distrobox:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>

- Entra em um contêiner Distrobox e executa um comando no login:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Entra em um contêiner Distrobox sem instanciar um tty:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_contêiner</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
