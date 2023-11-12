---
layout: page
title: common/du (português (Brasil))
description: "Uso de disco: estima e sumariza o uso de espaço em disco de arquivos e diretórios."
content_hash: 3230b6abf024398fc71a3b1a27423fce2a904254
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

Uso de disco: estima e sumariza o uso de espaço em disco de arquivos e diretórios.
Mais informações: <https://www.gnu.org/software/coreutils/du>.

- Lista os tamanhos dos diretórios e qualquer subdiretório, em uma unidade de tamanho (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Lista os tamanhos dos diretórios e subdiretórios, em tamanho legívell por humanos (isto é seleciona automaticamente a unidade de tamanho apropriada para o tamanho):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Exibe o tamanho de um único diretório, em tamanho legível por humanos:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Lista em tamanho legível por humanos todos os arquivos e diretórios dentro de um diretório:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Lista em tamanho legível por humanos, até o nível N de profundidade um diretório e subdiretórios:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Lista em tamanho legível por humanos todos os arquivos `.jpg` dos subdiretórios do diretório atual, e exibe o total cumulativo no final:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
