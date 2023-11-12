---
layout: page
title: windows/ipconfig (italiano)
description: "Mostra e gestisce le configurazioni di rete di Windows."
content_hash: 6484714414d7a09cf782c31bb85d39246f4c70d3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ipconfig

Mostra e gestisce le configurazioni di rete di Windows.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Mostra la lista delle schede di rete:

`ipconfig`

- Mostra la lista dettagliata delle schede di rete:

`ipconfig /all`

- Rinnova l'indirizzo IP di una scheda di rete:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheda_di_rete</span>

- Libera gli indirizzi IP per una scheda di rete:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheda_di_rete</span>

- Rimuovi tutti i dati dalla cache DNS:

`ipconfig /flushdns`
