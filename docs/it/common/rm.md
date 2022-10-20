---
layout: page
title: common/rm (italiano)
description: "Rimuovi file o directory."
content_hash: 4bd10fac043a2f900e647ea5ddd6b46181e4ab25
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
---
# rm

Rimuovi file o directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/rm>.

- Rimuovi file:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1 percorso/del/file2 ...</span>

- Rimuovi ricorsivamente una directory e tutti i suoi contenuti:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Rimuovi ricorsivamente una directory, senza chiedere conferma o mostrare messaggi di errore:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Rimuovi file interattivamente, chiedendo conferma prima di rimuovere ogni file:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file(s)</span>

- Rimuovi file in modalità verbosa, scrivendo un messaggio a schermo per ogni file rimosso:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
