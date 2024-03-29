---
layout: page
title: common/pcapfix (Deutsch)
description: "Repariere beschädigte oder korrumpierte `pcap`- und `pcapng`-Dateien."
content_hash: 9b527d61fd31087fc3a68271254496c548d024ca
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/common/pcapfix.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pcapfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pcapfix

Repariere beschädigte oder korrumpierte `pcap`- und `pcapng`-Dateien.
Weitere Informationen: <https://f00l.de/pcapfix/>.

- Repariere eine `pcap`/`pcapng`-Datei (Hinweis: bei `pcap`-Dateien werden nur die ersten 262144 Bytes jedes Pakets gescannt):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.pcapng</span>

- Repariere eine ganze `pcap`-Datei:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.pcap</span>

- Repariere eine `pcap`/`pcapng`-Datei und schreibe die Reparieree Datei an einen bestimmten Speicherort:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/Repariere.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.pcap</span>

- Behandle die zu reparierende Datei als `pcapng`-Datei, unabhängig von der automatischen Typenerkennung:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.pcapng</span>

- Repariere eine Datei und zeige den Reparaturprozess im Detail:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.pcap</span>
