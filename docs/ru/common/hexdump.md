---
layout: page
title: common/hexdump (русский)
description: "Дамп файла в ASCII, десятичном, шестнадцатеричном и восьмеричном форматах."
content_hash: 076490840d253ed91c23bf13f42b0727cd29977f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexdump

Дамп файла в ASCII, десятичном, шестнадцатеричном и восьмеричном форматах.
Больше информации: <https://manned.org/hexdump>.

- Распечатать шестнадцатеричное представление файла, заменяя повторяющиеся строки на '*':

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Отобразить шестнадцатеричное и ASCII представление в две колонки:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Отобразить двухколончатое представление файла, обработав только указанное число байтов с начала:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">количество_байтов</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>

- Не заменять повторяющиеся строки на '*':

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/файла</span>
