---
layout: page
title: common/which (русский)
description: "Отобразить абсолютный путь к программе."
content_hash: 53b7249580eddf043f327f9172370017e126b85e
last_modified_at: 2023-01-07
related_topics:
  - title: English version
    url: /en/common/which.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/which.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/which.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/which.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># which

Отобразить абсолютный путь к программе.
Больше информации: <https://manned.org/which>.

- Найти переменную окружения PATH и отобразить расположение всех соответствующих исполняемых файлов:

`which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">исполняемый_файл</span>

- Если есть несколько исполняемых файлов, которые совпадают, отобразить все:

`which -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">исполняемый_файл</span>
