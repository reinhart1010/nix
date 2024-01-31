---
layout: page
title: osx/afplay (italiano)
description: "Riproduttore audio a riga di comando."
content_hash: 995495301ecf242bd1ade64099b0e706b73a90de
last_modified_at: 2024-01-31
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
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/afplay.1.html>.

- Riproduci un file audio (fino a quando non finisce la riproduzione):

`afplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci un file audio al doppio della velocità:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci un file audio alla metà della velocità:

`afplay --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riproduci i primi N secondi di un file audio:

`afplay --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
