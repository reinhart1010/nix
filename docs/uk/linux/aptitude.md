---
layout: page
title: linux/aptitude (українська)
description: "Утиліта керування пакетами Debian і Ubuntu."
content_hash: 18f0835ef22577ace53dd450f7ca18d30a248451
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Утиліта керування пакетами Debian і Ubuntu.
Більше інформації: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Синхронізувати список доступних пакетів і версій. Це слід запустити спочатку, перш ніж запускати наступні команди aptitude:

`aptitude update`

- Встановити новий пакет і його залежності:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Шукати пакет:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Шукати встановлений пакет (`?installed` це термін пошуку aptitude):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>`)'`

- Видалити пакет і всі залежні від нього пакети:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Оновити встановлені пакети до найновіших доступних версій:

`aptitude upgrade`

- Оновити встановлені пакети (як `aptitude upgrade`) включно з видаленням застарілих пакетів і встановленням додаткових, щоб відповідати новим залежностям пакетів:

`aptitude full-upgrade`

- Затримати встановлений пакет, щоб уникнути його автоматичного оновлення:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>`)'`
