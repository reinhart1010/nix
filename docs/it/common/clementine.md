---
layout: page
title: common/clementine (italiano)
description: "Un moderno player e gestore di librerie musicali."
content_hash: 6bd785431e82feb44f668ca2d178ae13d5036462
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/clementine.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clementine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clementine

Un moderno player e gestore di librerie musicali.
Maggiori informazioni: <https://github.com/clementine-player/Clementine/wiki>.

- Avvia l'interfaccia grafica oppure lo mette in evidenza:

`clementine`

- Avvia la riproduzione di un file musicale:

`clementine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|percorso/del/file/music.ext</span>

- Pausa o riprende la riproduzione:

`clementine --play-pause`

- Ferma la riproduzione:

`clementine --stop`

- Passa alla traccia successiva o precedente:

`clementine --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">next|previous</span>

- Crea una nuova playlist con uno o più file musicali oppure URL:

`clementine --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url1 url2 ... | percorso/del/file/music1.ext percorso/del/file/music2.ext ...</span>

- Carica una playlist:

`clementine --load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file/playlist.ext</span>

- Riproduce una specifica traccia nella playlist caricata:

`clementine --play-track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
