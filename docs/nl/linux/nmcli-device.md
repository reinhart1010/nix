---
layout: page
title: linux/nmcli-device (Nederlands)
description: "Beheer netwerkinterfaces en zetten nieuwe Wi-Fi-verbindingen op via NetworkManager."
content_hash: 4397d57d08ebda15283b7b093ea53ddb80307952
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/nmcli-device.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmcli-device.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli device

Beheer netwerkinterfaces en zetten nieuwe Wi-Fi-verbindingen op via NetworkManager.
Dit subcommando kan ook aangeroepen worden met `nmcli d`.
Meer informatie: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Toon de statussen van alle netwerkinterfaces:

`nmcli device status`

- Toon alle beschikbare WiFi-toegangspunten:

`nmcli device wifi`

- Verbind met een Wi-Fi netwerk via een gespecificeerd SSID (je zal gevraagd worden voor een wachtwoord):

`nmcli --ask device wifi connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssid</span>

- Toon het wachtwoord en de QR-code voor het huidige Wi-Fi netwerk:

`nmcli device wifi show-password`
