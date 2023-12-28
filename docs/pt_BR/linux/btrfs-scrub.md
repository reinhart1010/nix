---
layout: page
title: linux/btrfs-scrub (português (Brasil))
description: "Varre os sistemas de arquivos btrfs para verificar a integridade dos dados."
content_hash: 2630d1cdfb62db087e310b1e9484350f68b538d1
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/btrfs-scrub.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/btrfs-scrub.html
    icon: bi bi-globe
tldri18n_status: 2
---
# btrfs scrub

Varre os sistemas de arquivos btrfs para verificar a integridade dos dados.
Recomenda-se fazer uma varredura uma vez por mês.
Mais informações: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Começar uma varredura:

`sudo btrfs scrub start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>

- Mostra o status de uma varredura em andamento ou concluída:

`sudo btrfs scrub status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>

- Cancela uma varredura em andamento:

`sudo btrfs scrub cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>

- Retoma uma varredura cancelada anteriormente:

`sudo btrfs scrub resume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>

- Inicia uma varredura, mas espera até que a varredura termine antes de sair:

`sudo btrfs scrub start -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>

- Inicia uma varredura no modo silencioso (não imprime erros ou estatísticas):

`sudo btrfs scrub start -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ponto_de_montagem_btrfs</span>
