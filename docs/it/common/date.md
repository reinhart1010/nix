---
layout: page
title: common/date (italiano)
description: "Imposta o mostra data e ora di sistema."
content_hash: 81c0cb949663ca50c89ba844cb0e0be96874cff6
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/date.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/date.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/date.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Imposta o mostra data e ora di sistema.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Mostra la data corrente utilizzando il formato predefinito della locale corrente:

`date +"%c"`

- Mostra la data corrente in UTC e formato ISO 8601:

`date -u +"%Y-%m-%dT%H:%M:%S%Z"`

- Mostra la data corrente come timestamp Unix (secondi dall'epoca Unix):

`date +%s`

- Mostra una specifica data (rappresentata come timestamp Unix) utilizzando il formato predefinito:

`date -d @1473305798`

- Converti una specifica data in un timestamp Unix:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`
