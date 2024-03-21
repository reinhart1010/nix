---
layout: page
title: common/scamper (Deutsch)
description: "Sondiert aktiv das Internet, um die Topologie und Leistung zu analysieren."
content_hash: 911b4af7128438e373c6e354228711d6ffc3cc84
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/common/scamper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scamper

Sondiert aktiv das Internet, um die Topologie und Leistung zu analysieren.
Liefert einige Werkzeuge mit, welche mit `sc_` starten, beispielsweise `sc_warts2text` oder `sc_ttlexp`.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Führe die Standardoption (Traceroute) auf ein Ziel aus:

`scamper -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>

- Führe zwei Aktionen (ping und traceroute) auf zwei verschiedenen Zielen aus:

`scamper -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`" -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>

- Pinge mehrere Hosts mit UDP an, verwende eine bestimmte Portnummer für den ersten Ping und erhöhe sie für jeden weiteren Ping:

`scamper -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UDP-dport</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33434</span>`" -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>

- Verwende den Multipath Discovery Algorithm (MDA), um das Vorhandensein von lastverteilten Pfaden zum Ziel zu ermitteln, und verwende für die Sondierung ICMP-Echopakete mit maximal drei Versuchen, und schreibe das Ergebnis in eine `warts`-Datei:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracelb</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ICMP-echo</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`"`

- Führe eine Paris-Traceroute mit ICMP zu einem Ziel aus und speichere das Ergebnis in einer komprimierten `warts`-Datei:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts.gz</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">icmp-paris</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beaf::4</span>`"`

- Zeichne alle ICMP-Pakete, die an einer bestimmten IP-Adresse ankommen und eine bestimmte ICMP-ID haben, in einer `warts`-Datei auf:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -I "sniff -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beef::6</span>` icmp[icmpid] == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101</span>`"`
