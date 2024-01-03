---
layout: page
title: common/git-check-ignore (italiano)
description: "Analizza ed esegui il debug di \".gitignore\" e dei file esclusi."
content_hash: 84243bc7f8fc32d5085f0aa9ad0012a8c05691da
last_modified_at: 2024-01-03
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
  - title: Türkçe version
    url: /tr/common/git-check-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-ignore

Analizza ed esegui il debug di ".gitignore" e dei file esclusi.
Maggiori informazioni: <https://git-scm.com/docs/git-check-ignore>.

- Verifica se un file o una directory sono ignorati:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Verifica se più file o directory sono ignorati:

`git check-ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...</span>

- Leggi i percorsi di file o directory da `stdin` (uno per riga) invece che dalla riga di comando:

`git check-ignore --stdin < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/lista_dei_file_o_directory</span>

- Non controllare nell'indice (usato per determinare il motivo per cui alcuni percorsi non sono ignorati):

`git check-ignore --no-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...</span>

- Includi dettagli sul pattern corrispondente per ogni percorso specificato:

`git check-ignore --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...</span>
