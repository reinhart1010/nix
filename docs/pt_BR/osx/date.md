---
layout: page
title: osx/date (português (Brasil))
description: "Define ou exibe a data do sistema."
content_hash: 2d4cc43573f94c406d8a38035785978ca9a58b57
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
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
Mais informações: <https://ss64.com/osx/date.html>.

- Exibe a data atual usando o formato da localidade padrão:

`date +%c`

- Exibe a data atual no formato UTC e ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Exibe a data atual como um timestamp Unix (segundos desde a época Unix):

`date +%s`

- Exibe uma data específica (representada como um timestamp Unix) usando o formato padrão:

`date -r 1473305798`
