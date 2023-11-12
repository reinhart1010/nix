---
layout: page
title: linux/nmcli-connection (Nederlands)
description: "Beheer verbindingen met NetworkManager."
content_hash: 1211e3136f1d6fecb92f617acb7dbcafb7954548
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-connection.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-connection.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli connection

Beheer verbindingen met NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli c`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon alle NetworkManager connecties (toont naam, UUID, type en apparaat):

`nmcli connection`

- Activeer een connectie:

`nmcli connection up uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Deactiveer een connectie:

`nmcli connection down uuid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- Maak een automatisch geconfigueeerde dual stack connectie:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto</span>

- Maak een statische IPv6-only connectie:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::2/64</span>` gw6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv6.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::1</span>` ipv4.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Maak een statische IPv4-only connectie:

`nmcli connection add ifname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ethernet</span>` ip4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.7/8</span>` gw4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv4.dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.1</span>` ipv6.method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignore</span>

- Maak een VPN connectie via OpenVPN vanuit een OVPN bestand:

`nmcli connection import type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openvpn</span>` file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/vpn_config.ovpn</span>
