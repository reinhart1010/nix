---
layout: page
title: common/adguardhome (русский)
description: "Программное обеспечение для блокировки рекламы и отслеживания во всей сети."
content_hash: 0aa4ffaed91c96b537b82ff32b773d74c01a6e8d
related_topics:
  - title: English version
    url: /en/common/adguardhome.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adguardhome.html
    icon: bi bi-globe
---
# AdGuardHome

Программное обеспечение для блокировки рекламы и отслеживания во всей сети.
Больше информации: <https://github.com/AdguardTeam/AdGuardHome>.

- Запустить AdGuard Home:

`AdGuardHome`

- Запустить AdGuard с заданной конфигурацией:

`AdGuardHome --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/AdGuardHome.yaml</span>

- Установить рабочую папку, где будут сохранятья данные:

`AdGuardHome --work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">путь/до/папки</span>

- Установить или удалить AdGuard Home как службу:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>

- Запустить службу AdGuard Home:

`AdGuardHome --service start`

- Перезагрузить конфигурацию для службы AdGuard Home:

`AdGuardHome --service reload`

- Остановить или перезапустить службу AdGuard Home:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stop|restart</span>
