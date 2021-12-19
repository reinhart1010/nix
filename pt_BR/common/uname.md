---
layout: page
title: common/uname (português (Brasil))
description: "Apresenta detalhes sobre o hardware e sistema operacional do computador."
content_hash: 43f4c51a3e1ccd1eeb23709f4da24fbf7828e49c
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/uname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uname.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uname

Apresenta detalhes sobre o hardware e sistema operacional do computador.
Nota: Para maiores detalhes sobre o sistema operacional, utilize o comando `lsb_release`.
Mais informações: <https://www.gnu.org/software/coreutils/uname>.

- Exibir informações relacionadas ao hardware: arquitetura e tipo de processador:

`uname -mp`

- Exibir informações relacionadas ao software: sistema operacional, número da release e versão:

`uname -srv`

- Exibir o nome de rede do computador:

`uname -n`

- Exibir todas as informações disponíveis do sistema (hardware, software, nome de rede):

`uname -a`
