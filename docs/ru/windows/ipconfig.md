---
layout: page
title: windows/ipconfig (русский)
description: "Отображение и управление сетевыми настройками Windows."
content_hash: c8dd777cb2f70b76811ac88c35409382cc23841d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

Отображение и управление сетевыми настройками Windows.
Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Показать список сетевых адаптеров:

`ipconfig`

- Показать подробный список сетевых адаптеров:

`ipconfig /all`

- Обновить IP-адреса сетевого адаптера:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">адаптер</span>

- Освободить IP-адреса сетевого адаптера:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">адаптер</span>

- Удалить все данные из кеша DNS:

`ipconfig /flushdns`
