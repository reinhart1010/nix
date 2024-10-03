---
layout: page
title: linux/top (português (Brasil))
description: "Mostra informações, em tempo real, sobre os processos em execução."
content_hash: 697cfb0ca5cfe9ef7f65a5a633da680e40ca9851
last_modified_at: 2024-10-03
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Mostra informações, em tempo real, sobre os processos em execução.
Mais informações: <https://manned.org/top>.

- Inicia o `top`:

`top`

- Exibe apenas os processos ativos:

`top -i`

- Exibe os processos de um usuário específico:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Ordena os processos por campo:

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_campo</span>

- Mostra todas as threads de um dado processo:

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Mostra apenas processos com determinados PID(s), informados em uma lista separada por vírgulas (Normalmente você não saberá os PIDs de cabeça. Este exemplo pega os PIDs a partir do nome de um processo):

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_processo</span>`)`

- Mostra ajuda sobre comandos interativos:

`?`
