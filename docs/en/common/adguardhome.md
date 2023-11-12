---
layout: page
title: common/adguardhome (English)
description: "A network-wide software for blocking ads & tracking."
content_hash: b99fd5abef42609b60061fe0abef23ba14f767e5
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/adguardhome.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adguardhome.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adguardhome.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adguardhome.html
    icon: bi bi-globe
tldri18n_status: 2
---
# AdGuardHome

A network-wide software for blocking ads & tracking.
More information: <https://github.com/AdguardTeam/AdGuardHome>.

- Run AdGuard Home:

`AdGuardHome`

- Run AdGuard Home with a specific config:

`AdGuardHome --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/AdGuardHome.yaml</span>

- Set the work directory for data to be stored in:

`AdGuardHome --work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Install or uninstall AdGuard Home as a service:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>

- Start the AdGuard Home service:

`AdGuardHome --service start`

- Reload the configuration for the AdGuard Home service:

`AdGuardHome --service reload`

- Stop or restart the AdGuard Home service:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stop|restart</span>
