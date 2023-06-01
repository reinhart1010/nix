---
layout: page
title: common/adguardhome (Nederlands)
description: "Netwerkbrede software voor het blokkeren van advertenties en tracking."
content_hash: 2720aa721c1880dda91d71717164ac37aac4a0ec
last_modified_at: 2023-06-01
related_topics:
  - title: English version
    url: /en/common/adguardhome.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adguardhome.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adguardhome.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adguardhome.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># AdGuardHome

Netwerkbrede software voor het blokkeren van advertenties en tracking.
Meer informatie: <https://github.com/AdguardTeam/AdGuardHome>.

- Voer AdGuard Home uit:

`AdGuardHome`

- Voer AdGuard Home uit met een specifieke configuratie:

`AdGuardHome --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/AdGuardHome.yaml</span>

- Stel de werkdirectory in waarin gegevens moeten worden opgeslagen:

`AdGuardHome --work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>

- Installeer of verwijder AdGuard Home als een service:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>

- Start de AdGuard Home-service:

`AdGuardHome --service start`

- Laad de configuratie voor de AdGuard Home-service opnieuw:

`AdGuardHome --service reload`

- Stop of herstart de AdGuard Home-service:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stop|restart</span>
