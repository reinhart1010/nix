---
layout: page
title: windows/date (italiano)
description: "Mostra o imposta la data del sistema."
content_hash: 6f819aa08913678a07afbdd19aa5cded785cd663
last_modified_at: 2023-05-09
related_topics:
  - title: English version
    url: /en/windows/date.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Mostra o imposta la data del sistema.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/date>.

- Mostra la data corrente e chiedi di impostarne una nuova (lascia vuoto per lasciare quella corrente):

`date`

- Mostra la data corrente senza chiedere di impostarne una nuova:

`date /t`

- Cambia la data corrente a una data specifica:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mese</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">giorno</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">anno</span>
