---
layout: page
title: windows/netstat (Nederlands)
description: "Toon actieve TCP-verbindingen, poorten waarop de computer luistert, netwerkadapterstatistieken, de IP-routeringstabel, IPv4- en IPv6-statistieken."
content_hash: ac63374370422166ee8bb12cc505d3bfb417fb67
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/windows/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

Toon actieve TCP-verbindingen, poorten waarop de computer luistert, netwerkadapterstatistieken, de IP-routeringstabel, IPv4- en IPv6-statistieken.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>.

- Toon actieve TCP-verbindingen:

`netstat`

- Toon alle actieve TCP-verbindingen en de TCP- en UDP-poorten waarop de computer luistert:

`netstat -a`

- Toon netwerkadapterstatistieken, zoals het aantal verzonden en ontvangen bytes en pakketten:

`netstat -e`

- Toon actieve TCP-verbindingen en druk adressen en poortnummers numeriek uit:

`netstat -n`

- Toon actieve TCP-verbindingen en geef het proces-ID (PID) weer voor elke verbinding:

`netstat -o`

- Toon de inhoud van de IP-routeringstabel:

`netstat -r`

- Toon statistieken per protocol:

`netstat -s`

- Toon een lijst van momenteel open poorten en gerelateerde IP-adressen:

`netstat -an`
