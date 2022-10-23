---
layout: page
title: common/7za (português (Brasil))
description: "Um compactador de arquivos com alta taxa de compressão."
content_hash: 6720dfff60b1d134f9396e0315e8552a1a4e351d
related_topics:
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7za.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/7za.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># 7za

Um compactador de arquivos com alta taxa de compressão.
Versão compacta do `7z`, com suporte para menos tipos de arquivamento/compressão.
Mais informações: <https://www.7-zip.org>.

- Compactar um arquivo ou diretório:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Criptografa um arquivo existente (incluindo cabeçalhos):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` -mhe=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>

- Descompactar um arquivo mantendo a estrutura de diretórios original:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>

- Descompacta um arquivo em um diretório específicado pelo usuário:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Descompacta um arquivo para a saída padrão:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>` -so`

- Compacta utilizando um tipo específico de arquivamento/compressão:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zip|gzip|bzip2|tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/arquivo_ou_diretório</span>

- Exibe o conteúdo de um arquivo:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_compactado.7z</span>

- Exibe os tipos de arquivamento/compressão disponíveis:

`7za i`
