---
layout: page
title: common/date (Deutsch)
description: "Setze die Systemzeit oder zeige sie an."
content_hash: 0c2dc0275fbd0c9c2f8725425121de31a37e4f71
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
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
tldri18n_status: 2
---
# date

Setze die Systemzeit oder zeige sie an.
Weitere Informationen: <https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html>.

- Zeige das aktuelle Datum im Format der eingestellten Locale an:

`date +%c`

- Zeige das aktuelle Datum in koordinierter Weltzeit (UTC) im ISO 8601-Format an:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Zeige das aktuelle Datum in Unixzeit (vergangene Sekunden seit der Unix-Epoche) an:

`date +%s`

- Konvertiere ein in Unixzeit gegebenes Datum zum Standardformat:

`date -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>

- Konvertiere ein gegebenes Datum zu Unixzeit:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- Zeige das aktuelle Datum im RFC-3339 Format (`YYYY-MM-DD hh:mm:ss TZ`) an:

`date --rfc-3339 s`

- Setze das aktuelle Datum im Format `MMDDhhmmYYYY.ss` (`YYYY` und `.ss` sind optional):

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- Zeige die aktuelle ISO-Wochenzahl an:

`date +%V`
