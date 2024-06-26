---
layout: page
title: osx/date (português (Brasil))
description: "Define ou exibe a data do sistema."
content_hash: 33bbe9fcb209cc9047a6c6f6d2d88417505a62b7
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/date.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

Define ou exibe a data do sistema.
Mais informações: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Exibe a data atual usando o formato da localidade padrão:

`date +%c`

- Exibe a data atual no formato UTC e ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Exibe a data atual como um timestamp Unix (segundos desde a época Unix):

`date +%s`

- Exibe uma data específica (representada como um timestamp Unix) usando o formato padrão:

`date -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>
