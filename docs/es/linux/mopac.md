---
layout: page
title: linux/mopac (español)
description: "MOPAC (Molecular Orbital PACkage) es un programa semiempírico de química cuántica basado en la aproximación NDDO de Dewar y Thiel."
content_hash: 21dadb87279c71838426731efc73642f5f405ba3
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/mopac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mopac

MOPAC (Molecular Orbital PACkage) es un programa semiempírico de química cuántica basado en la aproximación NDDO de Dewar y Thiel.
Más información: <https://github.com/openmopac/mopac>.

- Realiza los cálculos a partir de un archivo de entrada (`.mop`, `.dat` y `.arc`):

`mopac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>

- Mínimo ejemplo de trabajo con HF que escribe en el directorio actual y lo guarda en el archivo de salida:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`
