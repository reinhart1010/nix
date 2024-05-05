---
layout: page
title: common/ack (italiano)
description: "Un tool di ricerca simile a `grep`, ottimizzato per programmatori."
content_hash: fe08b9c4aadb7acbc3e8cfbc1360a8f59d3fff36
last_modified_at: 2024-05-05
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Un tool di ricerca simile a `grep`, ottimizzato per programmatori.
Vedi anche: `rg`, che è molto più veloce.
Maggiori informazioni: <https://beyondgrep.com/documentation>.

- Cerca ricorsivamente file contenenti una stringa o un'espressione regolare nella directory corrente:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Cerca un pattern in modalità case-insensitive:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Cerca righe di testo contenenti un pattern, mostrando solo il testo corrispondente e non il resto della riga:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Limita la ricerca ai file di un tipo specifico:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Non cercare nei file di un tipo specifico:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Conta il numero totale di corrispondenze trovate:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Mostra i nomi dei file e il numero di corrispondenze per ogni singolo file:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Mostra la lista di tutti i valori che possono essere usati con `--type`:

`ack --help-types`
