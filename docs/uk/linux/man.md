---
layout: page
title: linux/man (українська)
description: "Форматування та відображення сторінок посібника."
content_hash: 2fc34dd95620246085fb3f18b4fa542bc4019679
last_modified_at: 2024-02-07
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/man.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># man

Форматування та відображення сторінок посібника.
Більше інформації: <https://manned.org/man>.

- Відобразити довідкову сторінку для команди:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Відобразити сторінку довідки для команди з розділу 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Відобразити усі доступні розділи для команди:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Відобразити шлях пошуку довідкових сторінок:

`man --path`

- Відобразити розташування довідкової сторінки, а не довідкову сторінку:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Відобразити довідкову сторінку з використанням певної локалі:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">локаль</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">команда</span>

- Знайти довідкові сторінки, які містять рядок пошуку:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">рядок_пошуку</span>`"`
