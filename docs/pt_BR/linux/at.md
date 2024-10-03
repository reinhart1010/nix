---
layout: page
title: linux/at (português (Brasil))
description: "Executa comandos em um determinado momento."
content_hash: 996386c3894075f0cc4eab1f24f4d7117e994615
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/at.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Executa comandos em um determinado momento.
Mais informações: <https://manned.org/at.1>.

- Inicia o prompt `at` para que um novo conjunto de comandos seja agendado, pressione `Ctrl + D` para salvar e sair:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Executa os comandos e envia o resultado por e-mail utilizando algum programa de envio de e-mail local, por exemplo o Sendmail:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -m`

- Executa um script em um determinado momento:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Mostra uma notificação de sistema às 23h em 18 de Fevereiro:

`echo "notify-send '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Acorda!</span>`'" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11pm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Feb 18</span>
