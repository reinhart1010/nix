---
layout: page
title: common/axel (português (Brasil))
description: "Acelerador de downloads."
content_hash: e53e8386ae563621c41e30306ca8a500fe53a1fa
last_modified_at: 2023-12-28
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

- Faz download de uma URL para um arquivo:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Faz download especificando o nome do arquivo de destino:

`axel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Faz download usando múltiplas conexões:

`axel -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_conexões</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Procura por mirrors:

`axel -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_mirrors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limita a velocidade de download (em bytes por segundo):

`axel -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidade</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
