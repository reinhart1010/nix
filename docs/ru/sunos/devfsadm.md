---
layout: page
title: sunos/devfsadm (русский)
description: "Команда администрирования для `/dev`. Поддерживает пространство имен `/dev`."
content_hash: 507a3f0909ed555aaf095d91b606f61c0eb836d5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

Команда администрирования для `/dev`. Поддерживает пространство имен `/dev`.
Больше информации: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Сканировать для новых дисков:

`devfsadm -c disk`

- Очистить все оборванные ссылки `/dev` и выполнить поиск нового устройства:

`devfsadm -C -v`

- Пробный-запуск - вывод того, что бы изменилось, но без произведения модификаций:

`devfsadm -C -v -n`
