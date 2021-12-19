---
layout: page
title: common/cake (italiano)
description: "Strumento da linea di comando per il framework CakePHP."
content_hash: 18fba045345d870883ffa03b089e0e166837253f
related_topics:
  - title: English version
    url: /en/common/cake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cake.html
    icon: bi bi-globe
---
# cake

Strumento da linea di comando per il framework CakePHP.
Maggiori informazioni: <https://cakephp.org>.

- Mostra informazioni sull'attuale app ed i comandi disponibili:

`cake`

- Elenca le rotte disponibili:

`cake routes`

- Pulisci le cache di configurazione:

`cake cache clear_all`

- Costruisci la cache dei metadati:

`cake schema_cache build --connection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">connessione</span>

- Pulisci la cache dei metadati:

`cake schema_cache clear`

- Pulisci una tabella di cache:

`cake schema_cache clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_tabella</span>

- Avvia un web server di sviluppo (porta predefinita 8765):

`cake server`

- Avvia una shell REPL interattiva:

`cake console`
