---
layout: page
title: common/lpstat (português (Brasil))
description: "Exibe informações sobre o estado de impressoras."
content_hash: 9d6d618a4eeee3277c45caafa1b1a26364149943
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lpstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpstat

Exibe informações sobre o estado de impressoras.
Mais informações: <https://manned.org/lpstat>.

- Lista impressoras presentes na máquina e se estão habilitadas para impressão:

`lpstat -p`

- Exibe a impressora padrão:

`lpstat -d`

- Exibe todas as informações de estado disponíveis:

`lpstat -t`

- Mostra uma lista de trabalhos de impressão que foram colocados na fila pelo usuário especificado:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>
