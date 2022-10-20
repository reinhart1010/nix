---
layout: page
title: common/ack (italiano)
description: "Un tool di ricerca simile a `grep`, ottimizzato per programmatori."
content_hash: 5f837dad5963f0c191924a7c63155be57911470d
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
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

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>

- Non cercare nei file di un tipo specifico:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>

- Conta il numero totale di corrispondenze trovate:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Mostra i nomi dei file e il numero di corrispondenze per ogni singolo file:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_ricerca</span>`"`

- Mostra la lista di tutti i valori che possono essere usati con `--type`:

`ack --help-types`
