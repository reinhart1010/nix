---
layout: page
title: linux/nmcli-agent (español)
description: "Ejecuta `nmcli` como agente secreto de NetworkManager o agente polkit."
content_hash: 5e31679c38ca249b1fa3a84b88f4a995816d2da8
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/linux/nmcli-agent.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/nmcli-agent.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/nmcli-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmcli agent

Ejecuta `nmcli` como agente secreto de NetworkManager o agente polkit.
Este subcomando también se puede llamar con `nmcli a`.
Más información: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Registra `nmcli` como agente secreto y escucha solicitudes secretas:

`nmcli agent secret`

- Registra `nmcli` como agente polkit y escucha solicitudes de autorización:

`nmcli agent polkit`

- Registra `nmcli` como agente secreto y agente de polkit:

`nmcli agent all`
