---
layout: page
title: common/eslint (italiano)
description: "Utilità di linting per JavaScript e JSX."
content_hash: 549b8b0b0164ae709df8710dac5388184ae8a061
last_modified_at: 2023-05-23
related_topics:
  - title: Deutsch version
    url: /de/common/eslint.html
    icon: bi bi-globe
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

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.js percorso/del/file2.js ...</span>

- Risolvi gli errori di linting:

`eslint --fix`

- Esegui il linting utilizzando un determinato file di configurazione:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.js percorso/del/file2.js ...</span>
