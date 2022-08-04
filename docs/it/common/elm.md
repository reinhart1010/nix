---
layout: page
title: common/elm (italiano)
description: "Compila ed esegui file sorgente Elm."
content_hash: c99f6fa1dab7ed1c9a0a2e00bafa25f872b539e0
related_topics:
  - title: English version
    url: /en/common/elm.html
    icon: bi bi-globe
---
# elm

Compila ed esegui file sorgente Elm.
Maggiori informazioni: <https://elm-lang.org>.

- Inizializza un progetto Elm, generando un file `elm.json`:

`elm init`

- Avvia una shell Elm interattiva:

`elm repl`

- Compila un file Elm, scrivendo il risultato in un file `index.html`:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente</span>

- Compila un file Elm, scrivendo il risultato in un file JavaScript:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorgente</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destinazione</span>`.js`

- Avvia un web server locale che compila file Elm al caricamento delle pagine:

`elm reactor`

- Installa un pacchetto Elm da https://package.elm-lang.org:

`elm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
