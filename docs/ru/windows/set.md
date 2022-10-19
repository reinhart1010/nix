---
layout: page
title: windows/set (русский)
description: "Отобразить или задать значение переменным окружения для текущего экземпляра CMD."
content_hash: 6038cd1fb3b875d8c2661f3091e966cd220c7baa
related_topics:
  - title: English version
    url: /en/windows/set.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/set.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/set.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/set.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># set

Отобразить или задать значение переменным окружения для текущего экземпляра CMD.
Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/set>.

- Вывести список текущих переменных окружения:

`set`

- Задать переменной окружения определённое значение:

`set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">значение</span>

- Вывести список переменных окружения, имена которых начинаются с заданной строки:

`set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>

- Запросить у пользователя значение для указанной переменной:

`set /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">имя</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">строка_подсказки</span>
