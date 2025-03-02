---
layout: page
title: common/whatweb (español)
description: "Escáner web de nueva generación."
content_hash: 388333f49d793b6d867bd06c4f62ba32b45f1486
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/whatweb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# whatweb

Escáner web de nueva generación.
Más información: <https://morningstarsecurity.com/research/whatweb>.

- Escanea sitios web/objetivos en busca de tecnologías web:

`whatweb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website1 website2 ...</span>

- Lee objetivos/sitios web desde un archivo:

`whatweb -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_objetivos</span>

- Analiza un sitio web/objetivo en modo detallado:

`whatweb -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Ejecuta un escaneo agresivo en un sitio web:

`whatweb -a 3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Escanear una red y suprimir errores:

`whatweb --no-errors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.0/24</span>

- Lista de complementos:

`whatweb -l`

- Lista de complementos:

`whatweb -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_complemento</span>
