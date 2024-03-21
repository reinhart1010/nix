---
layout: page
title: common/sc_tracediff (Deutsch)
description: "Anzeige von Traceroute-Pfaden, bei denen sich der Pfad geändert hat."
content_hash: a1a83b41b85b8ce75b7ea63787926c45ec0c0f9e
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/common/sc_tracediff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc_tracediff

Anzeige von Traceroute-Pfaden, bei denen sich der Pfad geändert hat.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Zeige den Unterschied zwischen den traceroutes in zwei `warts`-Dateien:

`sc_tracediff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>

- Zeige den Unterschied zwischen den traceroutes in zwei `warts`-Dateien, einschließlich derer, die sich nicht geändert haben:

`sc_tracediff -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>

- Zeige den Unterschied zwischen den traceroutes in zwei `warts'-Dateien und versuche, wenn möglich, DNS-Namen und nicht IP-Adressen anzuzeigen:

`sc_tracediff -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.warts</span>
