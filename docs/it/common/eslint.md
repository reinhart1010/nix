---
layout: page
title: common/eslint (italiano)
description: "Utilità di linting per JavaScript e JSX."
content_hash: a9e5b70f5d75c93cbd5e51e3512708cdab98a8d7
related_topics:
  - title: English version
    url: /en/common/eslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/eslint.html
    icon: bi bi-globe
---
# eslint

Utilità di linting per JavaScript e JSX.
Maggiori informazioni: <https://eslint.org>.

- Crea una configurazione eslint:

`eslint --init`

- Esegui il linting di un dato set di file:

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.js file2.js</span>

- Risolvi gli errori di linting:

`eslint --fix`

- Esegui il linting utilizzando un determinato file di configurazione:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app/src</span>
