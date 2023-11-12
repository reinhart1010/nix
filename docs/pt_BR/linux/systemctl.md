---
layout: page
title: linux/systemctl (português (Brasil))
description: "Controla o sistema systemd e o gerenciador de serviços."
content_hash: 37f2bc30e7808459690f7bfff36659b3c5365770
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

Controla o sistema systemd e o gerenciador de serviços.
Mais informações: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostra todos os serviços em execução:

`systemctl status`

- Lista unidades com falha:

`systemctl --failed`

- Inicia/Para/Reinicia/Recarrega um serviço:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Mostra o status de uma unidade:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Ativa/Desativa uma unidade a ser iniciada na inicialização:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Mascara/Desmascara uma unidade para impedir ativação e ativação manual:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Recarrega o systemd, verificando por unidades novas ou alteradas:

`systemctl daemon-reload`

- Verifica se uma unidades está ativada:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>
