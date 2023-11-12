---
layout: page
title: linux/nmcli-radio (Nederlands)
description: "Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager."
content_hash: 386cfff0f2a442a492caaf996fe08f7a0d60b0f7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-radio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli radio

Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli r`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de status van Wi-Fi:

`nmcli radio wifi`

- Zet Wi-Fi aan of uit:

`nmcli radio wifi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Toon de status van WWAN:

`nmcli radio wwan`

- Zet WWAN aan of uit:

`nmcli radio wwan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Toon de status van beide switches:

`nmcli radio all`

- Zet beide switches aan of uit:

`nmcli radio all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
