---
layout: page
title: common/complete (italiano)
description: "Fornisce autocompletamento per argomenti dei comandi della shell."
content_hash: f7b0917522715ce72cd562111b3d4a9405232578
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/complete.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/complete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# complete

Fornisce autocompletamento per argomenti dei comandi della shell.
Maggiori informazioni: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- Applica ad un comando una funzione per gestirne l'autocompletamento:

`complete -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funzione</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Applica ad un comando un altro comando per gestirne l'autocompletamento:

`complete -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_per_autocompletamento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Applica l'autocompletamento senza aggiungere uno spazio dopo la parola completata:

`complete -o nospace -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">function</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
