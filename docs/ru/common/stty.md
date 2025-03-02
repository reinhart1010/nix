---
layout: page
title: common/stty (русский)
description: "Настройка параметров интерфейса терминального устройства."
content_hash: 12910df2cd0bb2b7d7fcfbdcabdfed9489f71d5d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/stty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># stty

Настройка параметров интерфейса терминального устройства.
Больше информации: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Показать все настройки для текущего терминала:

`stty --all`

- Задать количество строк или столбцов:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количество</span>

- Получить фактическую скорость передачи данных устройства:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_устройства</span>` speed`

- Сбросить все режимы до разумных значений для текущего терминала:

`stty sane`
