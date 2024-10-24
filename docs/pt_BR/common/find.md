---
layout: page
title: common/find (português (Brasil))
description: "Procura recursivamente por arquivos ou diretórios em uma árvore de diretórios."
content_hash: 55d06809358adf3bcb99706b2f8da01378f991ae
last_modified_at: 2024-10-24
related_topics:
  - title: English version
    url: /en/common/find.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/find.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/find.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/find.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/find.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/find.html
    icon: bi bi-globe
tldri18n_status: 2
---
# find

Procura recursivamente por arquivos ou diretórios em uma árvore de diretórios.
Mais informações: <https://manned.org/find>.

- Procura por arquivos pela extensão:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- Procura por arquivos que correspondam a vários padrões específicos de caminho/nome:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/caminho/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*nome*</span>`'`

- Procura por diretórios que correspondam a um nome específico, sem diferenciar maiúsculo de minúsculo:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*nome*</span>`'`

- Procura por arquivos que correspondam a um nome específico, excluindo certos caminhos:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/caminho/*</span>`'`

- Procura por arquivos que correspondam a uma faixa de tamanho específica, limitando a profundidade recursiva para "1":

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- Executa um comando para cada arquivo (use `{}` dentro do comando para acessar o nome do arquivo):

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l</span>` {} \;`

- Procura por todos os arquivos modificados hoje e passa os resultados para um único comando como argumentos:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -daystart -mtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cvf arquivo.tar</span>` {} \+`

- Procura por arquivos vazios (0 byte) ou diretórios e os exclui de forma verbosa:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_raiz</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|d</span>` -empty -delete -print`
