---
layout: page
title: linux/addr2line (português (Brasil))
description: "Converte endereços de um binário em nomes de arquivos e números de linha."
content_hash: 19052fb1c18af6f61188213b818d5969ee3535fd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/addr2line.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addr2line.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addr2line.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addr2line

Converte endereços de um binário em nomes de arquivos e números de linha.
Mais informações: <https://manned.org/addr2line>.

- Exibe o nome do arquivo e o número da linha do código-fonte de um endereço de instrução de um executável:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/executavel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco</span>

- Exibe o nome da função, nome do arquivo e número da linha:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/executavel</span>` --functions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco</span>

- Desembaraça o nome da função em código C++:

`addr2line --exe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/executavel</span>` --functions --demangle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereco</span>
