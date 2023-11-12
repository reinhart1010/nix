---
layout: page
title: common/history (español)
description: "Historial de la línea de comandos."
content_hash: f9b922ced0f05c5009dddbdc5eb71938edde1601
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history

Historial de la línea de comandos.
Más información: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Muestra el historial de comandos junto a su número de línea:

`history`

- Muestra los últimos 20 comandos:

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Limpia el historial de comandos (solo para la shell actual):

`history -c`

- Sobrescribe el archivo histórico con el historial de la shell actual (comúnmente se combina con `history -c` para limpiar el historial):

`history -w`

- Borra la entrada del historial en el índice especificado:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">indice</span>
