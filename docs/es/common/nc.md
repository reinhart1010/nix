---
layout: page
title: common/nc (español)
description: "Redirige datos de entrada o salida a un flujo de red a través de esta versátil herramienta."
content_hash: 28f57cad7951a7302dc0f4361cd64ff1c8294179
last_modified_at: 2024-06-21
related_topics:
  - title: English version
    url: /en/common/nc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nc

Redirige datos de entrada o salida a un flujo de red a través de esta versátil herramienta.
Más información: <https://manned.org/nc.1>.

- Inicia un escuchador en un puerto TCP y le envía un archivo:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo</span>

- Conecta a un escuchador en un puerto y recibe un archivo de él:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo_por_recibir</span>

- Escanea los puertos TCP abiertos en un host:

`nc -v -z -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_de_espera_en_segundos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_inicial</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_final</span>

- Inicia un escuchador en un puerto TCP y provee de acceso a tu intérprete de comandos local a la parte conectada (esto es peligroso y podría ser explotado):

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejecutable_del_intérprete</span>

- Conecta a un escuchador y provee de acceso a tu intérprete de comandos local a una parte remota (esto es peligroso y podría ser explotado):

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejecutable_del_intérprete</span>

- Actúa como un proxy y envía información de un puerto TCP local a un host remoto:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_local</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_remoto</span>

- Envía una petición HTTP GET:

`echo -e "GET / HTTP/1.1\nHost: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`\n\n" | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` 80`
