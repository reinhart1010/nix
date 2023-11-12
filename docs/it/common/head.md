---
layout: page
title: common/head (italiano)
description: "Stampa a schermo le prime linee di un file."
content_hash: d64363e1d571bfdecde74f90ac7401efb2d58447
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/head.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/head.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/head.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/head.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/head.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># head

Stampa a schermo le prime linee di un file.
Maggiori informazioni: <https://manned.org/head.1p>.

- Stampa a schermo le prime linee di un file:

`head -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_linee</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Stampa a schermo i primi byte di un file:

`head -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_byte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Stampa a schermo tutto il file meno le ultime linee:

`head -n -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_linee</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Stampa a schermo tutto il file meno gli ultimi byte:

`head -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_di_byte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
