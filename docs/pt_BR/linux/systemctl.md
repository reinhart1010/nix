---
layout: page
title: linux/systemctl (português (Brasil))
description: "Controla o sistema systemd e o gerenciador de serviços."
content_hash: bad1ed46adc8edf4749755d26c003d5146dfa71f
last_modified_at: 2024-10-02
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
  - title: 中文 version
    url: /zh/linux/systemctl.html
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

- Inicia/Para/Reinicia/Recarrega o estado um serviço:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Ativa/Desativa uma unidade a ser iniciada na inicialização:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Recarrega o systemd, verificando por unidades novas ou alteradas:

`systemctl daemon-reload`

- Verifica se uma unidade está ativada/ativa/em falha:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is-active|is-enabled|isfailed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>

- Lista todos as unidades de serviço/socket/auto-montável filtrando por estado executando/falhou:

`systemctl list-units --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|socket|automount</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">failed|running</span>

- Mostra o conteúdo e o caminho absoluto do arquivo de uma unidade:

`systemctl cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidade</span>
