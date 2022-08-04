---
layout: page
title: common/dust (português (Brasil))
description: "Dust oferece uma visão geral de quais diretórios estão usando espaço em disco."
content_hash: 73e03ee09a46daa278f6b3f6c1d381ca8749a984
related_topics:
  - title: English version
    url: /en/common/dust.html
    icon: bi bi-globe
---
# dust

Dust oferece uma visão geral de quais diretórios estão usando espaço em disco.
Mais informações: <https://github.com/bootandy/dust>.

- Exibe informações para o diretório atual:

`dust`

- Exibe informações para uma lista de diretórios separados por espaço:

`dust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório2</span>

- Exibe 30 diretórios (o padrão é 21):

`dust --number-of-lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Exibe informações para o diretório atual, com até 3 níveis de profundidade:

`dust --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Exibe os maiores diretórios no topo em ordem decrescente:

`dust --reverse`

- Ignora todos os arquivos e diretórios com um nome específico:

`dust --ignore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_ou_nome_do_diretório</span>

- Não exibe barras de porcentagem e porcentagens:

`dust --no-percent-bars`
