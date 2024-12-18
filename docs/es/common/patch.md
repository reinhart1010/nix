---
layout: page
title: common/patch (español)
description: "Emparcha un archivo (o archivos) con un archivo diff."
content_hash: ac897d5dbe60a5e63b2a145ea446aa65964bc7b6
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/patch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/patch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# patch

Emparcha un archivo (o archivos) con un archivo diff.
Ten en cuenta que los archivos diff deben ser generados por el comando `diff`.
Más información: <https://manned.org/patch>.

- Aplica un parche usando un archivo diff (los nombres de archivo deben incluirse en el archivo diff):

`patch < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parche.diff</span>

- Aplica un parche a un archivo específico:

`patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parche.diff</span>

- Emparcha un archivo escribiendo el resultado a un archivo diferente:

`patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_entrada</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parche.diff</span>

- Aplica un parche al directorio actual:

`patch -p1 < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parche.diff</span>

- Aplica el reverso de un parche:

`patch -R < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parche.diff</span>
