---
layout: page
title: linux/dpkg-query (italiano)
description: "Uno strumento che mostra informazioni sui pacchetti installati."
content_hash: cc5d151e1bbb15e4df021864759972fd353c27b9
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/dpkg-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dpkg-query

Uno strumento che mostra informazioni sui pacchetti installati.
Maggiori informazioni: <https://manned.org/dpkg-query.1>.

- Elenca tutti i pacchetti installati:

`dpkg-query -l`

- Elenca i pacchetti installati con nomi che combaciano con una data espressione:

`dpkg-query -l '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_pattern</span>`'`

- Elenca tutti i file installati da una pacchetto:

`dpkg-query -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Mostra le informazioni riguardanti un pacchetto:

`dpkg-query -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>
