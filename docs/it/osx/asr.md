---
layout: page
title: osx/asr (italiano)
description: "Ripristina (copia) un'immagine disco dentro a un volume."
content_hash: 5abe99c2affb20481ff38fa069dc64e1f4019336
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/asr.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/asr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/asr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/asr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asr

Ripristina (copia) un'immagine disco dentro a un volume.
Il nome del comando sta per Apple Software Restore (software di ripristino Apple).
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- Ripristina un'immagine disco su un volume specifico:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_immagine.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/volume</span>

- Distruggi il volume specifico prima di ripristinare:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_immagine.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/volume</span>` --erase`

- Salta la verifica dopo il ripristino:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_immagine.dmg</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/volume</span>` --noverify`

- Clona i volumi senza utilizzare un'immagine disco intermedia:

`sudo asr restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/volume</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/volume/clonato</span>
