---
layout: page
title: common/unrar (português (Brasil))
description: "Descompactar arquivos comprimidos no formato RAR."
content_hash: 541ce8c43eeac5ce5694fd2c56ff8fd7b52e04d4
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/unrar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/unrar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unrar

Descompactar arquivos comprimidos no formato RAR.
Mais informações: <https://manned.org/unrar>.

- Descompacta o arquivo mantendo a estrutura de diretórios original:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rar</span>

- Descompacta o arquivo para um caminho especificado mantendo a estrutura de diretórios original:

`unrar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/extrair</span>

- Descompacta o arquivo sem manter a estrutura de diretórios original:

`unrar e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rar</span>

- Verifica a integridade do conteúdo de um arquivo:

`unrar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rar</span>

- Exibe o conteúdo de um arquivo sem descompactá-lo:

`unrar l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rar</span>
