---
layout: page
title: common/ansiweather (English)
description: "A shell script for displaying the current weather conditions in your terminal."
content_hash: 1b698c812a0165a3430159b7ffff5e0c9efc642b
last_modified_at: 2024-02-06
related_topics:
  - title: Deutsch version
    url: /de/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ansiweather

A shell script for displaying the current weather conditions in your terminal.
More information: <https://github.com/fcambus/ansiweather>.

- Display a [f]orecast using metric [u]nits for the next seven days for a specific [l]ocation:

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Display a [F]orecast for the next five days showing [s]ymbols and [d]aylight data for your current location:

`ansiweather -F -s true -d true`

- Display today's [w]ind and [h]umidity data for your current location:

`ansiweather -w true -h true`
