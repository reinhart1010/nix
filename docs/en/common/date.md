---
layout: page
title: common/date (English)
description: "Set or display the system date."
content_hash: e199ff5601b8ee691e35c52ff9c393841829310c
related_topics:
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
---
# date

Set or display the system date.
More information: <https://www.gnu.org/software/coreutils/date>.

- Display the current date using the default locale's format:

`date +%c`

- Display the current date in UTC, using the ISO 8601 format:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Display the current date as a Unix timestamp (seconds since the Unix epoch):

`date +%s`

- Convert a date specified as a Unix timestamp to the default format:

`date -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>

- Convert a given date to the Unix timestamp format:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- Display the current date using the RFC-3339 format (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`

- Set the current date using the format `MMDDhhmmYYYY.ss` (`YYYY` and `.ss` are optional):

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- Display the current ISO week number:

`date +%V`
