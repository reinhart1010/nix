---
layout: page
title: common/git-check-ignore (italiano)
description: "Analizza ed esegui il debug di \".gitignore\" e dei file esclusi."
content_hash: ad04eedf2acf4822e07647147bf62702ba8ed4aa
related_topics:
  - title: English version
    url: /en/common/git-check-ignore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-check-ignore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-check-ignore.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-check-ignore.html
    icon: bi bi-globe
---
# git check-ignore

Analizza ed esegui il debug di ".gitignore" e dei file esclusi.
Maggiori informazioni: <https://git-scm.com/docs/git-check-ignore>.

- Verifica se un file o una cartella sono ignorati:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_o_cartella</span>

- Verifica se più file o cartelle sono ignorati:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/cartella</span>

- Leggi i percorsi di file o cartelle da stdin (uno per riga) invece che dalla riga di comando:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/lista_dei_file_o_cartelle</span>

- Non controllare nell'indice (usato per determinare il motivo per cui alcuni percorsi non sono ignorati):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorsi/ai/file_o_cartelle</span>

- Includi dettagli sul pattern corrispondente per ogni percorso specificato:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorsi/ai/file_o_cartelle</span>
