---
layout: page
title: osx/log (italiano)
description: "Visualizza, esporta e configura i sistemi di log."
content_hash: 10c8022d297bacd8912415cba9de9fcbae8b2f80
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/osx/log.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># log

Visualizza, esporta e configura i sistemi di log.
Maggiori informazioni: <https://www.dssw.co.uk/reference/log.html>.

- Mostra i log di sistema in diretta:

`log stream`

- Mostra i log mandati a `syslog` da processi con un PID specifico:

`log stream --process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ID_processo</span>

- Mostra i log mandati a `syslog` da processi con un nome specifico:

`log show --predicate "process == '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`'"`

- Esporta sul disco tutti i log dell'ultima ora:

`sudo log collect --last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1h</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.logarchive</span>
