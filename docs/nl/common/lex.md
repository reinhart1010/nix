---
layout: page
title: common/lex (Nederlands)
description: "Generator voor lexicale analyzers."
content_hash: bf13f31919f8cee08ce97bcf5b50de786db220d2
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/common/lex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lex

Generator voor lexicale analyzers.
Gegeven de specificatie voor een lexicale analyzer, genereert C-code die deze implementeert.
Opmerking: op de meeste grote besturingssystemen is dit commando een alias voor `flex`.
Meer informatie: <https://manned.org/lex.1>.

- Genereer een analyzer van een Lex-bestand en sla deze op in het bestand `lex.yy.c`:

`lex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>

- Specificeer het uitvoerbestand:

`lex -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.l</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer.c</span>

- Compileer een C-bestand dat door Lex is gegenereerd:

`c99 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/lex.yy.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoerbaar_bestand</span>
