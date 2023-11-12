---
layout: page
title: common/stty (русский)
description: "Настройка параметров интерфейса терминального устройства."
content_hash: bc5c5219098e465b75ca5c0a9fcf46c900a240ee
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stty

Настройка параметров интерфейса терминального устройства.
Больше информации: <https://www.gnu.org/software/coreutils/stty>.

- Показать все настройки для текущего терминала:

`stty --all`

- Задать количество строк или столбцов:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количество</span>

- Получить фактическую скорость передачи данных устройства:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла_устройства</span>` speed`

- Сбросить все режимы до разумных значений для текущего терминала:

`stty sane`
