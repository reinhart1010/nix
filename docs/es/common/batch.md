---
layout: page
title: common/batch (español)
description: "Ejecuta comandos en un momento posterior cuando los niveles de carga del sistema lo permitan."
content_hash: bd1914f82caa55f3076465f1a1153140d6868a84
last_modified_at: 2024-12-20
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# batch

Ejecuta comandos en un momento posterior cuando los niveles de carga del sistema lo permitan.
Los resultados serán enviados al correo del usuario.
Vea también: `at`, `atq`, `atrm` `mail`.
Más información: <https://manned.org/batch>.

- Lanza el servicio `atd`:

`systemctl start atd`

- Ejecuta comandos de `stdin` (presiona `Ctrl + D` cuando hayas finalizado):

`batch`

- Ejecuta un comando desde `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./hacer_copia_de_la_bd.sh</span>`" | batch`
