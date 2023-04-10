---
layout: page
title: common/npx (italiano)
description: "Esegue file binari dai pacchetti `npm`."
content_hash: 9d99224609da6375fd5c0437afa972f0279bd0ed
last_modified_at: 2023-04-10
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
---
# npx

Esegue file binari dai pacchetti `npm`.
Maggiori informazioni: <https://github.com/npm/npx>.

- Esegue un file binario di uno specifico modulo:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argomenti_comando</span>

- Nel caso in cui ci siano più binari per lo stesso modulo, specifica il pacchetto da eseguire:

`npx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_modulo</span>

- Lancia un comando unicamente se questo esiste nel path corrente o in `node_modules/.bin`:

`npx --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argomenti_comando</span>

- Esegue il file binario del modulo specificato evitando di mostrare l'output prodotto dallo stesso `npx`:

`npx --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argomenti_comando</span>

- Mostra il menù d'aiuto:

`npx --help`
