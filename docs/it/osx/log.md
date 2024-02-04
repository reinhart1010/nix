---
layout: page
title: osx/log (italiano)
description: "Visualizza, esporta e configura i sistemi di log."
content_hash: 5dfae49bc841bd9170442b7664380733b75d486f
last_modified_at: 2024-02-04
related_topics:
  - title: English version
    url: /en/osx/log.html
    icon: bi bi-globe
tldri18n_status: 2
---
# log

Visualizza, esporta e configura i sistemi di log.
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/log.1.html>.

- Mostra i log di sistema in diretta:

`log stream`

- Mostra i log mandati a `syslog` da processi con un PID specifico:

`log stream --process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID_processo</span>

- Mostra i log mandati a `syslog` da processi con un nome specifico:

`log show --predicate "process == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`'"`

- Esporta sul disco tutti i log dell'ultima ora:

`sudo log collect --last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.logarchive</span>
