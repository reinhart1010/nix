---
layout: page
title: linux/lsblk (українська)
description: "Показує інформацію про пристрої."
content_hash: b44f972ca05a7c4280f6ee4cb2666a2ca9362802
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/lsblk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsblk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/lsblk.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsblk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsblk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsblk

Показує інформацію про пристрої.
Більше інформації: <https://manned.org/lsblk>.

- Показати усі пристрої зберігання даних у деревоподібному форматі:

`lsblk`

- Також показати порожні пристрої:

`lsblk -a`

- Показати стовпець SIZE у байтах, а не у форматі, зрозумілому людині:

`lsblk -b`

- Вивести інформацію про файлові системи:

`lsblk -f`

- Використати символи ASCII для форматування дерева:

`lsblk -i`

- Вивести інформацію про топологію блочного пристрою:

`lsblk -t`

- Виключити пристрої, указані в розділеному комами списку основних номерів пристроїв:

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7,...</span>

- Вивести налаштований підсумок за допомогою розділеного комами списку стовпців:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME,SERIAL,MODEL,TRAN,TYPE,SIZE,FSTYPE,MOUNTPOINT,...</span>
