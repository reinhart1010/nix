---
layout: page
title: linux/at (português (Brasil))
description: "Executa comandos em um determinado momento."
content_hash: b0857f9d9fa40ebe8b4851f39c1362b6bf2e5788
related_topics:
  - title: English version
    url: /en/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/at.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># at

Executa comandos em um determinado momento.
Mais informações: <https://man.archlinux.org/man/at.1>.

- Iniciar o prompt `at` para que um novo conjunto de comandos seja agendado, pressione `Ctrl + D` para salvar e sair:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>

- Executar os comandos e enviar o resultado por e-mail utilizando algum programa de envio de e-mail local, por exemplo o sendmail:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>` -m`

- Executar um script em um determinado momento:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm:ss</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_o_script</span>
