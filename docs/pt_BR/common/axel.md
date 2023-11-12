---
layout: page
title: common/axel (português (Brasil))
description: "Acelerador de downloads."
content_hash: 0dec7a621b9004a66f758e8cb3e2e2fe1fac7e76
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/axel.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/axel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/axel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/axel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/axel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/axel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# axel

Acelerador de downloads.
Suporta HTTP, HTTPS, e FTP.
Mais informações: <https://github.com/axel-download-accelerator/axel>.

- Fazer download de uma URL para um arquivo:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Fazer download especificando o nome do arquivo de destino:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Fazer download usando múltiplas conexões:

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_conexões</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Procurar por mirrors:

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_mirrors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limitar velocidade de download (em bytes por segundo):

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidade</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
