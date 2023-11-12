---
layout: page
title: common/mpv (italiano)
description: "Un player audio/video basato su MPlayer."
content_hash: 4943a862cffff72e8635c0c8711724e15e600e89
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mpv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mpv

Un player audio/video basato su MPlayer.
Maggiori informazioni: <https://mpv.io>.

- Riproduci un file video o audio:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Salta avanti/indietro di 5 secondi:

`SINISTRA <oppure> DESTRA`

- Salta indietro/avanti di 1 minuto:

`GIÙ <oppure> SU`

- Riduci o aumenta la velocità di riproduzione del 10%:

`[ <oppure> ]`

- Riproduci un file a una velocità specifica (da 0.01 a 100, normalmente 1):

`mpv --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocità</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Riproduci un file usando un profilo definito nel file `mpv.conf`:

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_profilo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
