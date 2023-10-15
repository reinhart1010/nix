---
layout: page
title: common/uname (português (Brasil))
description: "Exibe detalhes sobre a máquina atual e o sistema operacional em execução nela."
content_hash: 4d7d991669445ae34f9bb4667baff6d774d18401
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/uname.html
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

Exibe detalhes sobre a máquina atual e o sistema operacional em execução nela.
Veja também `lsb_release`.
Mais informações: <https://www.gnu.org/software/coreutils/uname>.

- Exibe o nome do kernel:

`uname`

- Exibe informações sobre a arquitetura e o processador:

`uname --machine --processor`

- Exibe nome do kernel, lançamento do kernel e versão do kernel:

`uname --kernel-name --kernel-release --kernel-version`

- Exibe o nome de rede do computador:

`uname --nodename`

- Exibe todas as informações disponíveis sobre o sistema:

`uname --all`
