---
layout: page
title: linux/pacman (українська)
description: "Утиліта для керування пакетами Arch Linux."
content_hash: 6fdc28fa3eb9dced22fab8b2fd90324db83104d0
last_modified_at: 2024-09-25
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/pacman.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/pacman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman

Утиліта для керування пакетами Arch Linux.
Дивіться також: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
Для еквівалентних команд в інших менеджерах пакетів дивіться <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Більше інформації: <https://manned.org/pacman.8>.

- Синхронізувати та оновити всі пакети:

`sudo pacman -Syu`

- Встановити новий пакет:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Видалити пакет і його залежності:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">пакет</span>

- Шукати в базі даних пакети, що містять певний файл:

`pacman -F "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ім'я_файлу</span>`"`

- Перелічити встановлені пакети та версії:

`pacman -Q`

- Перелічити лише явно встановлені пакети та версії:

`pacman -Qe`

- Перелічити безхазяйні пакети (встановлені як залежні, але фактично не потрібних для жодного пакета):

`pacman -Qtdq`

- Очистити весь кеш Pacman:

`sudo pacman -Scc`
