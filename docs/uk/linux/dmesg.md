---
layout: page
title: linux/dmesg (українська)
description: "Відобразити повідомлення ядра в `stdout`."
content_hash: fe55c681dd1a965253347174b9e5ae1199c48a12
last_modified_at: 2023-10-21
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dmesg

Відобразити повідомлення ядра в `stdout`.
Більше інформації: <https://manned.org/dmesg>.

- Відобразити повідомлення ядра:

`dmesg`

- Відобразити повідомлення про помилки ядра:

`dmesg --level err`

- Відобразити повідомлення ядра та продовжити читати нові, подібно до `tail -f` (доступно в ядрах 3.5.0 і новіших):

`dmesg -w`

- Відобразити, скільки фізичної пам'яті доступно в цій системі:

`dmesg | grep -i memory`

- Відобразити повідомлення ядра по 1 сторінці за раз:

`dmesg | less`

- Відобразити повідомлення ядра з міткою часу (доступно в ядрах 3.5.0 і новіших):

`dmesg -T`

- Відобразити повідомлення ядра у формі, зрозумілій людині (доступно в ядрах 3.5.0 і новіших):

`dmesg -H`

- Розфарбувати виведені дані (доступно в ядрах 3.5.0 і новіших):

`dmesg -L`
