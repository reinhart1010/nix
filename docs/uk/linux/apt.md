---
layout: page
title: linux/apt (українська)
description: "Утиліта керування пакетами для дистрибутивів на основі Debian."
content_hash: 3719e962f5687d9378d6781e3ae5ab3f45836401
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Утиліта керування пакетами для дистрибутивів на основі Debian.
Рекомендована заміна для `apt-get` при інтерактивному використанні в Ubuntu версії 16.04 і пізніших.
Еквівалентні команди в інших менеджерах пакунків дивитися <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Більше інформації: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Оновити список доступних пакетів і версій (рекомендується запускати це перед іншими командами `apt`):

`sudo apt update`

- Шукати заданий пакет:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Відобразити інформацію про пакет:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Встановити пакет або оновити його до останньої доступної версії:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет (використання `purge` натомість також видаляє його конфігураційні файли):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Оновити усі встановлені пакети до найновіших доступних версій:

`sudo apt upgrade`

- Відобразити список усіх пакетів:

`apt list`

- Відобразити список усіх встановлених пакетів:

`apt list --installed`
