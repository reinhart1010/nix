---
layout: page
title: common/blackfire (italiano)
description: "Strumento di profilazione da linea di comando per PHP."
content_hash: ddfa39586ade74f64e59a65d88c4d42a080d7a94
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/blackfire.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/blackfire.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blackfire

Strumento di profilazione da linea di comando per PHP.
Maggiori informazioni: <https://blackfire.io>.

- Inizializza e configura il client Blackfire:

`blackfire config`

- Lancia l'agent Blackfire:

`blackfire agent`

- Lancia l'agent Blackfire su uno specifico socket:

`blackfire agent --socket="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp://127.0.0.1:8307</span>`"`

- Lancia il profiler su uno specifico programma:

`blackfire run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php percorso/del/file.php</span>

- Lancia il profiler e raccogli 10 campioni:

`blackfire --samples 10 run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php percorso/del/file.php</span>

- Lancia il profiler e mostra i risultati in output come JSON:

`blackfire --json run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php percorso/del/file.php</span>

- Carica un file del profiler sul servizio web di Blackfire:

`blackfire upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Mostra lo stato dei profili sul servizio web di Blackfire:

`blackfire status`
