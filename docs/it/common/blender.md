---
layout: page
title: common/blender (italiano)
description: "Interfaccia da linea di comando per il programma di grafica Blender 3D."
content_hash: 92bdfca923b91d511f27fb0d50ce1aa9842836f5
last_modified_at: 2023-04-17
related_topics:
  - title: English version
    url: /en/common/blender.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/blender.html
    icon: bi bi-globe
---
# blender

Interfaccia da linea di comando per il programma di grafica Blender 3D.
Gli argomenti sono eseguiti nell'ordine in cui sono dati.
Maggiori informazioni: <https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html>.

- Renderizza tutti i frame di una animazione in background, senza caricare l'interfaccia grafica (l'output è salvato in `/tmp`):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend -a`

- Renderizza un'animazione usando uno specifico pattern, in un percorso relativo (`//`) al file `.blend`:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">render/frame_###.png</span>` -a`

- Renderizza il decimo frame di un'animazione come singola immagine, salvandolo in una directory esistente (percorso assoluto):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/percorso/della/directory_output</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Renderizza il penultimo frame di un'animazione come immagine JPEG, salvandolo in una directory esistente (path relativa al file):

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend -o //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory_output</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-2</span>

- Renderizza l'animazione di una specifica scena, dal frame 10 al 500:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_scena</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>` -a`

- Renderizza un'animazione ad una specifica risoluzione, attraverso l'utilizzo di uno script python:

`blender -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>`.blend --python-expr '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import bpy; bpy.data.scenes[0].render.resolution_percentage = 25</span>`' -a`

- Avvia una sessione interattiva di Blender nel terminale con una console python (esegui `import bpy` dopo l'avvio):

`blender -b --python-console`
