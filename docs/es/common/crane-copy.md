---
layout: page
title: common/crane-copy (español)
description: "Copia eficientemente una imagen remota de origen a destino conservando el valor de resumen."
content_hash: 12920094e77bb341af949ffcafa96e8c2dd3cba2
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/common/crane-copy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-copy.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/crane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane copy

Copia eficientemente una imagen remota de origen a destino conservando el valor de resumen.
Más información: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Copia una imagen de origen a destino:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>

- Copia todas las etiquetas:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--all-tags</span>

- Establece el número máximo de copias simultáneas, predeterminados a GOMAXPROCS:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Evita sobrescribir las etiquetas existentes en el destino:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--no-clobber</span>

- Muestra la ayuda:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
