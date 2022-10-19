---
layout: page
title: windows/nvm (русский)
description: "Установка, удаление и переключение между версиями Node.js."
content_hash: 7e0e9b0e4b50ce742cac2d10c66a39c9859e1a1d
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nvm

Установка, удаление и переключение между версиями Node.js.
Поддерживает номера версий вроде "12.8" or "v16.13.1", метки вроде "stable", "system", и т.д.
Больше информации: <https://github.com/coreybutler/nvm-windows>.

- Установить заданную версию Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">версия_node</span>

- Задать версию Node.js по умолчанию (требуется запускать из-под Администратора):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">версия_node</span>

- Вывести список всех доступных версий Node.js и подсветить версию по умолчанию:

`nvm list`

- Удалить указанную версию Node.js:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">версия_node</span>
