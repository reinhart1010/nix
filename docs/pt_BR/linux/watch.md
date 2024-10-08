---
layout: page
title: linux/watch (português (Brasil))
description: "Executa um comando repetidas vezes, e monitora a saída em tela cheia."
content_hash: 7081dd9af4cae7251ad603202ebf59bded3ab4a1
last_modified_at: 2024-10-03
related_topics:
  - title: Deutsch version
    url: /de/linux/watch.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# watch

Executa um comando repetidas vezes, e monitora a saída em tela cheia.
Mais informações: <https://manned.org/watch>.

- Monitora arquivos no diretório atual:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Monitora espaço em disco e destaca as alterações:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- Monitora processos "node", atualizando a cada 3 segundos:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux | grep node</span>`"`

- Monitora o espaço em disco, e se ele mudar, para de monitorar:

`watch -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>
