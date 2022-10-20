---
layout: page
title: common/blackfire (italiano)
description: "Strumento di profilazione da linea di comando per PHP."
content_hash: 07a5cf8490ddbe092035a7d59eb666832b15a422
related_topics:
  - title: English version
    url: /en/common/blackfire.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/blackfire.html
    icon: bi bi-globe
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

`blackfire --samples=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php percorso/del/file.php</span>

- Lancia il profiler e mostra i risultati in output come JSON:

`blackfire --json run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php percorso/del/file.php</span>

- Carica un file del profiler sul servizio web di Blackfire:

`blackfire upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Mostra lo stato dei profili sul servizio web di Blackfire:

`blackfire status`
