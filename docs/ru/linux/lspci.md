---
layout: page
title: linux/lspci (русский)
description: "Отобразить список всех подключенных PCI-устройств."
content_hash: c94b9c5dcee4d818aaf14484516c6a58337d5af5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/lspci.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lspci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lspci

Отобразить список всех подключенных PCI-устройств.
Больше информации: <https://manned.org/lspci>.

- Отобразить список всех подключенных PCI-устройств:

`lspci`

- Показать дополнительную информацию:

`lspci -v`

- Отобразить драйверы и модули, работающие с каждым устройством:

`lspci -k`

- Отобрзить определённое устройство:

`lspci -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:18.3</span>

- Вывести информацию в удобном формате для чтения:

`lspci -vm`
