---
layout: page
title: common/boot (italiano)
description: "Strumenti di implementazione per il linguaggio di programmazione Clojure."
content_hash: 9dc9dc01dbdf8f1f94e454d424d253307cf46466
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/boot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/boot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# boot

Strumenti di implementazione per il linguaggio di programmazione Clojure.
Maggiori informazioni: <https://github.com/boot-clj/boot>.

- Avvia una sessione REPL con il progetto o autonomamente (standalone):

`boot repl`

- Implementa un singolo `uberjar`:

`boot jar`

- Genera lo scheletro di un nuovo progetto basato su un modello di codice esistente:

`boot --dependencies boot/new new --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_modello</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_progetto</span>

- Implementa l'ambiente di sviluppo (se si sta utilizzando il modello di codice boot/new):

`boot dev`

- Implementa l'ambiente di produzione (se si sta utilizzando il modello di codice boot/new):

`boot prod`

- Mostra la descrizione di uno specifico comando:

`boot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task</span>` --help`
