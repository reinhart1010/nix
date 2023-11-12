---
layout: page
title: common/boot (italiano)
description: "Strumenti di build per il linguaggio di programmazione Clojure."
content_hash: a337d349e71e7e57d3cb8bd2716baef187d26c1c
last_modified_at: 2023-11-12
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

Strumenti di build per il linguaggio di programmazione Clojure.
Maggiori informazioni: <https://github.com/boot-clj/boot>.

- Avvia una sessione REPL con il progetto o da sola:

`boot repl`

- Builda un singolo `uberjar`:

`boot jar`

- Mostra aiuto per un comando:

`boot cljs --help`

- Genera le fondamenta per un nuovo progetto basandoti su una template:

`boot --dependencies boot/new new --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_template</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_progetto</span>

- Builda per development (se si sta utilizzando il template boot/new):

`boot dev`

- BUilda per produzione (se si sta utilizzando il template boot/new):

`boot prod`
