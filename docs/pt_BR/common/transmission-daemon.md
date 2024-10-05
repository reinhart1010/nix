---
layout: page
title: common/transmission-daemon (português (Brasil))
description: "Daemon controlado com `transmission-remote` ou sua interface web."
content_hash: ddb6f742daf125ba5390934fb029719249348f10
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/transmission-daemon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-daemon

Daemon controlado com `transmission-remote` ou sua interface web.
Veja também: `transmission`.
Mais informações: <https://manned.org/transmission-daemon>.

- Inicia uma sessão headless `transmission`:

`transmission-daemon`

- Inicia e acompanha um diretório específico por novos torrents:

`transmission-daemon --watch-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Despeja configurações do daemon em formato JSON:

`transmission-daemon --dump-settings > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.json</span>

- Inicia com configurações específicas para a interface web:

`transmission-daemon --auth --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9091</span>` --allowed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>
