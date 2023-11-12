---
layout: page
title: common/alex (italiano)
description: "Uno strumento per individuare frasi scritte in modo insensibile o sconsiderato."
content_hash: 674ac1756d0afb1b7235684dea691ea32d5c2edf
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alex

Uno strumento per individuare frasi scritte in modo insensibile o sconsiderato.
Aiuta a trovare termini che favoriscono un certo genere, legati alla razza, religiosamente inappropriati, o simili termini non equi in un testo.
Maggiori informazioni: <https://github.com/get-alex/alex>.

- Analizza testo da standard input:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Frase da analizzare</span>` | alex --stdin`

- Analizza tutti i file nella directory corrente:

`alex`

- Analizza uno specifico file:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.md</span>

- Analizza tutti i file Markdown eccetto `esempio.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">esempio.md</span>
