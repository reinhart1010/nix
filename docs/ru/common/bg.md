---
layout: page
title: common/bg (русский)
description: "Возобновляет работу приостановленного задания (например, с помощью `Ctrl + Z`), и оставляет его работать в фоне."
content_hash: eaa57c0e948a5e686e7f65e584bad3cf4a1f760b
related_topics:
  - title: English version
    url: /en/common/bg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/bg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bg.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/bg.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/bg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bg

Возобновляет работу приостановленного задания (например, с помощью `Ctrl + Z`), и оставляет его работать в фоне.
Больше информации: <https://manned.org/bg>.

- Возобновить работу последнего приостановленного задания и продолжить его выполнение в фоне:

`bg`

- Возобновить указанное задание (используйте `jobs -l`, чтобы получить его идентификатор) и продолжить его выполнение в фоне:

`bg %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">идентификатор_задания</span>
