---
layout: page
title: osx/date (English)
description: "Set or display the system date."
content_hash: 3f4cbdbd7a71dde2357f34f7b7a7fd0d7153e96d
last_modified_at: 2023-11-12
related_topics:
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

Set or display the system date.
More information: <https://ss64.com/osx/date.html>.

- Display the current date using the default locale's format:

`date +%c`

- Display the current date in UTC and ISO 8601 format:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Display the current date as a Unix timestamp (seconds since the Unix epoch):

`date +%s`

- Display a specific date (represented as a Unix timestamp) using the default format:

`date -r 1473305798`
