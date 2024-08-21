---
layout: page
title: linux/lex (Nederlands)
description: "Generator voor lexicale analyzers."
content_hash: 337f235dabc6817d56271954d9720965600331d5
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/linux/lex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lex

Generator voor lexicale analyzers.
Gegeven de specificatie voor een lexicale analyzer, genereert C-code die deze implementeert.
Meer informatie: <https://manned.org/lex.1>.

- Genereer een analyzer van een Lex-bestand en sla deze op in het bestand `lex.yy.c`:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Schrijf de analyzer naar `stdout`:

`lex -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-stdout|t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Specificeer het uitvoerbestand:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.c</span>

- Genereer een [B]atch-scanner in plaats van een interactieve scanner:

`lex -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Compileer een C-bestand dat door Lex is gegenereerd:

`cc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lex.yy.c</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>
