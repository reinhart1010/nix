---
layout: page
title: common/cradle-elastic (Deutsch)
description: "Verwalte ElasticSearch Instanzen einer Cradle Instanz."
content_hash: 5ef640928b8190f72654c5d36441457c1e9269cf
related_topics:
  - title: English version
    url: /en/common/cradle-elastic.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-elastic.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-elastic.html
    icon: bi bi-globe
---
# cradle elastic

Verwalte ElasticSearch Instanzen einer Cradle Instanz.
Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Entleere den ElasticSearch Index:

`cradle elastic flush`

- Entleere den ElasticSearch Index für ein bestimmtes Paket:

`cradle elastic flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Sende ein ElasticSearch Schema ab:

`cradle elastic map`

- Sende ein ElasticSearch Schema für ein bestimmtes Paket ab:

`cradle elastic map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Befülle die ElasticSearch Indizes für alle Pakete:

`cradle elastic populate`

- Befülle die ElasticSearch Indizes für ein bestimmtes Paket:

`cradle elastic populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>
