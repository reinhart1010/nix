---
layout: page
title: common/file (italiano)
description: "Determina il tipo di file."
content_hash: 08ed583aedbc0c46ff0fb109bafc590e29160a23
related_topics:
  - title: Deutsch version
    url: /de/common/file.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/file.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># file

Determina il tipo di file.
Maggiori informazioni: <https://manned.org/file>.

- Fornisce una descrizione del tipo di file specificato. Funziona anche con file senza estensione:

`file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Controlla dentro un file zip e determina il tipo dei file in esso contenuti:

`file -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.zip</span>

- Permette a `file` di leggere file speciali o di dispositivo:

`file -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Non si limita al primo tipo di file trovato; continua a leggere il file fino alla fine:

`file -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Determina il tipo MIME di un file:

`file -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
