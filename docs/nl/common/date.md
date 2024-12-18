---
layout: page
title: common/date (Nederlands)
description: "Stel de systeemdatum in of toon deze."
content_hash: 4f9e1fd565cefe019cd5ff7da760c89cdc89aea0
last_modified_at: 2024-12-18
related_topics:
  - title: Deutsch version
    url: /de/common/date.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/date.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

Stel de systeemdatum in of toon deze.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Toon de huidige datum in het standaardformaat van de locale:

`date +%c`

- Toon de huidige datum in UTC, in het ISO 8601-formaat:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Toon de huidige datum als een Unix timestamp (seconden sinds de Unix-epoch):

`date +%s`

- Converteer een datum gespecificeerd als een Unix timestamp naar het standaard formaat:

`date -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>

- Converteer een opgegeven datum naar het Unix timestamp formaat:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- Toon de huidige datum in het RFC-3339 formaat (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339 s`

- Stel de huidige datum in met het formaat `MMDDhhmmYYYY.ss` (`YYYY` en `.ss` zijn optioneel):

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- Toon het huidige ISO-weeknummer:

`date +%V`
