---
layout: page
title: common/history (español)
description: "Historial de la línea de comandos."
content_hash: de0f174b8d07069634097e7d204afb930a5f25b1
last_modified_at: 2024-11-03
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
  - title: 한국어 version
    url: /ko/common/history.html
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

- Muestra los últimos 20 comandos (en Zsh muestra todos los comandos a partir del 20):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Muestra el historial con marcas de tiempo (timetamps) en diferentes formatos (solo disponible en Zsh):

`history -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|f|i|E</span>

- Limpia ([c]lean) el historial de comandos (solo para la interfaz de comandos actual):

`history -c`

- Sobrescribe (over[w]rite) el archivo histórico con el historial de la sesión actual (comúnmente se combina con `history -c` para limpiar el historial):

`history -w`

- Borra ([d]elete) la entrada del historial en el índice especificado:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">índice</span>
