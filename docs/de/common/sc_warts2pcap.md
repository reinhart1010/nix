---
layout: page
title: common/sc_warts2pcap (Deutsch)
description: "Schreibt die in den `warts`-Dateien enthaltenen Pakete in eine `pcap`-Datei."
content_hash: f830ff7cc8a1970983f1979a7623875f30f63349
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/common/sc_warts2pcap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc_warts2pcap

Schreibt die in den `warts`-Dateien enthaltenen Pakete in eine `pcap`-Datei.
Dies ist nur bei tbit, sting und sniff möglich.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Wandle die Daten aus mehreren `warts`-Dateien in eine `pcap`-Datei um:

`sc_warts2pcap -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts path/to/file2.warts ...</span>

- Wandle die Daten aus einer `warts`-Datei in eine `pcap`-Datei um und sortiere die Pakete nach Zeitstempel:

`sc_warts2pcap -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.warts</span>
