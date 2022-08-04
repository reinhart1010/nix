---
layout: page
title: common/history (português (Brasil))
description: "Histórico de linha da comando."
content_hash: 923ca02711dcd76f9cf5109075d02f728b58df02
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
---
# history

Histórico de linha da comando.
Mais informações: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Exibe a lista de histórico de comandos com números de linha:

`history`

- Exibe os últimos 20 comandos (em `zsh` ele exibe todos os comandos a partir do 20º):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Limpa a lista do histórico de comandos (apenas para o shell `bash` atual):

`history -c`

- Sobrescreve o arquivo de histórico com o histórico do shell `bash` atual (frequentemente combinado com `history -c` para limpar o histórico):

`history -w`

- Deleta a entrada do histórico no deslocamento especificado:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deslocamento</span>
