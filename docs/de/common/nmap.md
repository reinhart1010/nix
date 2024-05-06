---
layout: page
title: common/nmap (Deutsch)
description: "Netzwerk-Erkundungs-Werkzeug und Security / Port Scanner."
content_hash: d370d6ecacc4d227fcc7a29253240252c95d793e
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmap

Netzwerk-Erkundungs-Werkzeug und Security / Port Scanner.
Manche Funktionen können nur benutzt werden, wenn Nmap mit Root Rechten ausgeführt wird.
Weitere Informationen: <https://nmap.org/book/man.html>.

- Überprüfe ob eine IP-Adresse online ist und versuche, das Betriebssystem herauszufinden:

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_oder_hostname</span>

- Überprüfe nur ob die angegebenen Hosts online sind (Ping Scan) und ihre Domain-Namen:

`sudo nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_oder_hostname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_noch_eine_addresse</span>

- Scanne zusätzlich mit Skripten, Service-Erkennung, Betriebssystem-Fingerprinting und Traceroute:

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>

- Scanne eine spezifische Liste an Ports (benutze '-p-' für alle Ports von 1 bis 65535):

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2,...,portN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>

- Führe Dienst- und Versions-Erkennung auf den top 1000 Ports mit den Standard NSE Skripten aus; und schreibe das Ergebnis ('-oN') in der Ausgabe Datei:

`nmap -sC -sV -oN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ergebnis.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>

- Scanne Ziel(e) vorsichtig mit 'default and safe' NSE Scripts:

`nmap --script "default and safe" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>

- Scanne einen Web-Server, der auf den Standard Ports 80 und 443 läuft, mit allen verfügbaren 'http-*' NSE Skripten:

`nmap --script "http-*" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>` -p 80,443`

- Führe einen sehr langsamen verborgenen Scan ('-T0') aus um die Entdeckung von IDS/IPS zu umgehen und benutze Köder IP-Adressen ('-D'):

`nmap -T0 -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">köder1_ipaddresse,köder2_ipaddresse,...,köderN_ipaddresse</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">addresse_oder_addressen</span>
