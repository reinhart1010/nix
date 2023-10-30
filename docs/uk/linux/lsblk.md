---
layout: page
title: linux/lsblk (українська)
description: "Показує інформацію про пристрої."
content_hash: 923fba81851958b75291a68e566d5859f6ba65c7
last_modified_at: 2023-10-30
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

`lsblk -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,7</span>

- Вивести налаштований підсумок за допомогою розділеного комами списку стовпців:

`lsblk --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NAME</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SERIAL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MODEL</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TRAN</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIZE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FSTYPE</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">MOUNTPOINT</span>
