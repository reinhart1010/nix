---
layout: page
title: windows/set (русский)
description: "Отобразить или задать значение переменным окружения для текущего экземпляра CMD."
content_hash: 6038cd1fb3b875d8c2661f3091e966cd220c7baa
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/set.html
    icon: bi bi-globe
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
tldri18n_status: 2
---
# set

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
