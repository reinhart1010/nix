---
layout: page
title: common/beanstalkd (italiano)
description: "Un semplice e generico gestore di code di lavoro."
content_hash: 9aa77ce7fc20b8dea31a8286c87b7ab8727cdc74
related_topics:
  - title: English version
    url: /en/common/beanstalkd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/beanstalkd.html
    icon: bi bi-globe
---
# beanstalkd

Un semplice e generico gestore di code di lavoro.
Maggiori informazioni: <https://beanstalkd.github.io/>.

- Avvia beanstalkd, ascoltando sulla porta 11300:

`beanstalkd`

- Avvia beanstalkd ascoltando su porta ed un indirizzo dati:

`beanstalkd -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indirizzo_ip</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_porta</span>

- Rendi le code di lavoro persistenti salvandole su disco:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_persistente</span>

- Sincronizza con una directory persistente ogni 500 millisecondi:

`beanstalkd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_persistente</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
