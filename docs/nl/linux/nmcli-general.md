---
layout: page
title: linux/nmcli-general (Nederlands)
description: "Beheer algemene instellingen van NetworkManager."
content_hash: 75440653d428d0b5b51d77b247dd01ec25f2eced
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-general.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli general

Beheer algemene instellingen van NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli g`.
Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Toon de algemene status van NetworkManager:

`nmcli general`

- Toon de hostname van het huidige apparaat:

`nmcli general hostname`

- Verander de hostname van het huidige apparaat:

`sudo nmcli general hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_hostname</span>

- Toon de permissies van NetworkManager:

`nmcli general permissions`

- Toon het huidige logging level en domeinen:

`nmcli general logging`

- Zet het logging level en/of domainen (zie `man NetworkManager.conf` voor alle beschikbare domeinen):

`nmcli general logging level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">INFO|OFF|ERR|WARN|DEBUG|TRACE</span>` domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_1,domein_2,...</span>
