---
layout: page
title: osx/afplay (italiano)
description: "Riproduttore audio a riga di comando."
content_hash: 663e6491c88522132198a883a3e5692e94e1cc28
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/osx/afplay.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afplay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/afplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afplay

Riproduttore audio a riga di comando.
Maggiori informazioni: <https://ss64.com/osx/afplay.html>.

- Riproduci un file audio (fino a quando non finisce la riproduzione):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci un file audio al doppio della velocità:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci un file audio alla metà della velocità:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci i primi N secondi di un file audio:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
