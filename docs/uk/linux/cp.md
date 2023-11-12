---
layout: page
title: linux/cp (українська)
description: "Скопіювати файли і папки."
content_hash: baeb2a861bb1e5f8ecc5f8b6806961eed2ae4d0e
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Скопіювати файли і папки.
Більше інформації: <https://www.gnu.org/software/coreutils/cp>.

- Скопіювати файл в інше місце:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_який_скопіювати.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_в_який_скопіювати.ext</span>

- Скопіювати файл в іншу папку, зберугіючи назву файлу:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_який_скопіювати.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_в_яку_скопіювати</span>

- Рекурсивно скопіювати вміст папки до іншого місця (якщо місце призначення існує, папка скопіюється всередину нього):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/файлу_який_скопіювати</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_в_яку_скопіювати</span>

- Скопіювати папку рекурсивно у докладнішому режимі (показує файли у міру їх копіювання):

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_яку_спопіювати</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_в_яку_скопіювати</span>

- Скопіювати текстові файли в інше місце в інтерактивному режимі (запитує користувача перед перезаписом):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_в_яку_скопіювати</span>

- Зберігає символічні посилання(symbolic link) перед копіюванням:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">посилання</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/папки_в_яку_скопіювати</span>

- Використовує повний шлях файлу який потрібно скопіювати, створюючи будь-які відсутні проміжні папки під час копіювання:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">повний/шлях/до/файлу</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">шлях/до/бажаного_файлу</span>
