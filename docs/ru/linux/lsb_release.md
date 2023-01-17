---
layout: page
title: linux/lsb_release (русский)
description: "Выводит информацию, определённую стандартом LSB (Linux Standard Base), а также характерную для дистрибутива."
content_hash: ef5fdb4ffd259f1eee23cc7b3d115bb308ea1bf9
last_modified_at: 2023-01-17
related_topics:
  - title: català version
    url: /ca/linux/lsb_release.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsb_release.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsb_release.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lsb_release

Выводит информацию, определённую стандартом LSB (Linux Standard Base), а также характерную для дистрибутива.
Больше информации: <https://manned.org/lsb_release>.

- Отобразить всю имеющуюся информацию:

`lsb_release -a`

- Отобразить описание (обычно полное наименование) операционной системы:

`lsb_release -d`

- Отобразить наименование ОС, без указания поля "Distributor ID":

`lsb_release -i -s`

- Отобразить номер релиза (release number) и кодовое наименование дистрибутива без указания полей с названием:

`lsb_release -rcs`
