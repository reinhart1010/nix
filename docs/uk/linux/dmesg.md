---
layout: page
title: linux/dmesg (українська)
description: "Відобразити повідомлення ядра в `stdout`."
content_hash: 27648fc36094346e82c9c6e56dd6fd0b7eeaf46b
last_modified_at: 2024-09-30
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
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Відобразити повідомлення ядра в `stdout`.
Більше інформації: <https://manned.org/dmesg>.

- Відобразити повідомлення ядра:

`sudo dmesg`

- Відобразити повідомлення про помилки ядра:

`sudo dmesg --level err`

- Відобразити повідомлення ядра та продовжити читати нові, подібно до `tail -f` (доступно в ядрах 3.5.0 і новіших):

`sudo dmesg -w`

- Відобразити, скільки фізичної пам'яті доступно в цій системі:

`sudo dmesg | grep -i memory`

- Відобразити повідомлення ядра по 1 сторінці за раз:

`sudo dmesg | less`

- Відобразити повідомлення ядра з міткою часу (доступно в ядрах 3.5.0 і новіших):

`sudo dmesg -T`

- Відобразити повідомлення ядра у формі, зрозумілій людині (доступно в ядрах 3.5.0 і новіших):

`sudo dmesg -H`

- Розфарбувати виведені дані (доступно в ядрах 3.5.0 і новіших):

`sudo dmesg -L`
