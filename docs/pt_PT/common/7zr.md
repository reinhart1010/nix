---
layout: page
title: common/7zr (português (Portugal))
description: "Compactador de arquivos com uma alta taxa de compressão."
content_hash: 5e556bd2f1369e822b6f78f8b41f9e7205963d90
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7z

Compactador de arquivos com uma alta taxa de compressão.
Semelhante ao '7z', com a diferença que suporta apenas ficheiros '.7z'.
Mais informações: <https://manned.org/7zr>.

- Adicionar um ficheiro ou diretório a um novo ou existente arquivo:

`7z a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/ficheiro_ou_diretório</span>

- Encripa um arquivo existente (incluindo filenames):

`7z a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/ficheiro_encriptado.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palavra-passe</span>` -mhe=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7z x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>

- Descompactar um arquivo para um diretório especificado pelo utilizador:

`7z x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localização/do/directório</span>

- Descompactar um arquivo para a saída padrão (stdout):

`7z x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>` -so`

- Listar os conteúdos de um arquivo:

`7z l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório/arquivo_compactado.7z</span>

- Listar todos os tipos de arquivamento/compressão disponíveis:

`7z i`
