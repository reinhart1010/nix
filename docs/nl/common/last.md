---
layout: page
title: common/last (Nederlands)
description: "Bekijk de laatst ingelogde gebruikers."
content_hash: 49f5de525d956f4d370df701db39959578477c29
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/common/last.html
    icon: bi bi-globe
tldri18n_status: 2
---
# last

Bekijk de laatst ingelogde gebruikers.
Meer informatie: <https://manned.org/last>.

- Bekijk de laatste logins, hun duur en andere informatie uit `/var/log/wtmp`:

`last`

- Geef aan hoeveel van de laatste logins moeten worden weergegeven:

`last -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal_logins</span>

- Toon de volledige datum en tijd voor vermeldingen en toon vervolgens de hostnaam-kolom als laatste om afkapping te voorkomen:

`last -F -a`

- Bekijk alle logins van een specifieke gebruiker en toon het IP-adres in plaats van de hostnaam:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` -i`

- Bekijk alle geregistreerde herstarts (d.w.z. de laatste logins van de pseudo-gebruiker "reboot"):

`last reboot`

- Bekijk alle geregistreerde uitschakelingen (d.w.z. de laatste logins van de pseudo-gebruiker "shutdown"):

`last shutdown`
