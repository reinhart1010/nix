---
layout: page
title: linux/apt-get (українська)
description: "Утиліта керування пакетами Debian і Ubuntu."
content_hash: 795d9b61c17a7845a28568ba2050c3f0faa592c2
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Утиліта керування пакетами Debian і Ubuntu.
Шукати пакети за допомогою `apt-cache`.
Більше інформації: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Оновити список доступних пакетів і версій (рекомендується запускати це перед іншими командами `apt-get`):

`apt-get update`

- Встановити пакет або оновити його до останньої доступної версії:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет і файли його конфігурації:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Оновити усі встановлені пакети до найновіших доступних версій:

`apt-get upgrade`

- Очистити локальний репозиторій - видалити файли пакетів (`.deb`) із перерваних завантажень, які більше не можна завантажити:

`apt-get autoclean`

- Видалити усі пакети, які більше не потрібні:

`apt-get autoremove`

- Оновити встановлені пакети (як `upgrade`), але видалити застарілі пакети та встановити додаткові, щоб відповідати новим залежностям:

`apt-get dist-upgrade`
