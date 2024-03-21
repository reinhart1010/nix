---
layout: page
title: common/sc_wartsfilter (Deutsch)
description: "Filtert bestimmte Datensätze aus einer `warts`-Datei."
content_hash: a1f542eee2016feec967be59c5f53852f7d71d64
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/common/sc_wartsfilter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc_wartsfilter

Filtert bestimmte Datensätze aus einer `warts`-Datei.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Filtere alle Datensätze, welche ein bestimmtes Ziel haben und schreibe sie in eine separate Datei:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.5</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.6</span>

- Filtere alle Datensätze, welche ein Ziel in einem bestimmten Prefix haben und schreibe sie in eine separate Datei:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.warts</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8::/32</span>

- Filtere alle Datensätze, welche durch eine bestimmte Aktion entstanden sind und gebe sie als JSON aus:

`sc_wartsfilter -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.warts</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` | sc_warts2json`
