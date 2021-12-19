---
layout: page
title: linux/a2query (italiano)
description: "Recupera la configurazione di runtime da Apache su sistemi operativi basati su Debian."
content_hash: f216546e5245417b5005c487eb15a12cc8347483
related_topics:
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
---
# a2query

Recupera la configurazione di runtime da Apache su sistemi operativi basati su Debian.
Maggiori informazioni: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>.

- Lista i moduli Apache attivi:

`sudo a2query -m`

- Controlla se un modulo specifico è installato:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_modulo</span>

- Lista virtual host attivi:

`sudo a2query -s`

- Mostra il Modulo Multi-Processo correntemente attivo:

`sudo a2query -M`

- Mostra la versione di Apache:

`sudo a2query -v`
