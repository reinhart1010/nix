---
layout: page
title: osx/date (English)
description: "Set or display the system date."
content_hash: e9d8c8b121f2c39eeb341d61f38a209fa5f4c85b
related_topics:
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
---
# date

Set or display the system date.
More information: <https://ss64.com/osx/date.html>.

- Display the current date using the default locale's format:

`date +"%c"`

- Display the current date in UTC and ISO 8601 format:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- Display the current date as a Unix timestamp (seconds since the Unix epoch):

`date +%s`

- Display a specific date (represented as a Unix timestamp) using the default format:

`date -r 1473305798`
