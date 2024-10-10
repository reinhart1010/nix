---
layout: page
title: linux/nmcli-radio (Nederlands)
description: "Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager."
content_hash: 4baf8d96b439387cabc59a4436e823cfd120e554
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmcli-radio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli radio

Toon de status van radioschakelaars of schakel ze in/uit via NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli r`.
Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

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
