---
layout: page
title: common/gzip (português (Brasil))
description: "Compacta/descompacta arquivos com compressão gzip (LZ77)."
content_hash: ad61a4251313587ca9c7aeb5a7a877f48bd84e67
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/gzip.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gzip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gzip

Compacta/descompacta arquivos com compressão gzip (LZ77).
Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compacta um arquivo, substituindo-o por uma versão compactada gzip:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>

- Descompacta um arquivo, substituindo-o pela versão não compactada original:

`gzip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>`.gz`

- Compacta um arquivo, mantendo o arquivo original:

`gzip --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>

- Compacta um arquivo definindo o nome do arquivo de saída:

`gzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.ext.gz</span>

- Descompacta um arquivo gzip definindo o nome do arquivo de saída:

`gzip -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>`.gz > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_descompactado.ext</span>

- Especifica o nível de compactação. 1=mais rápido (pior), 9=mais lendo 9melhor, o nível padrão é 6:

`gzip -9 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.ext.gz</span>
