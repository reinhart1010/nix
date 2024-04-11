---
layout: page
title: common/pamslice (español)
description: "Extrae una línea de valores de una imagen PAM."
content_hash: 2a38c486c34f25da9a1e70c39bee0fe2abae51ac
last_modified_at: 2024-04-11
related_topics:
  - title: English version
    url: /en/common/pamslice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamslice

Extrae una línea de valores de una imagen PAM.
Más información: <https://netpbm.sourceforge.net/doc/pamslice.html>.

- Imprime los valores de los píxeles de la n-ésima fila en una tabla:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>

- Imprime los valores de los píxeles de la n-ésima columna de una tabla:

`pamslice -column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>

- Considera solo el m-ésimo plano de la imagen de entrada:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -plane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>

- Produce la salida en un formato adecuado para la entrada a un `xmgr` para la visualización:

`pamslice -row `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` -xmgr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/imagen.pam</span>
