---
layout: page
title: linux/at (português (Brasil))
description: "Executa comandos em um determinado momento."
content_hash: b0857f9d9fa40ebe8b4851f39c1362b6bf2e5788
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># at

Executa comandos em um determinado momento.
Mais informações: <https://man.archlinux.org/man/at.1>.

- Iniciar o prompt `at` para que um novo conjunto de comandos seja agendado, pressione `Ctrl + D` para salvar e sair:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>

- Executar os comandos e enviar o resultado por e-mail utilizando algum programa de envio de e-mail local, por exemplo o sendmail:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>` -m`

- Executar um script em um determinado momento:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_o_script</span>
