---
layout: page
title: common/gzip (português (Brasil))
description: "Ferramenta de compactação de arquivos com compressão gzip."
content_hash: 3f3f582db6936f073f0d61386b193d325594188c
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

Ferramenta de compactação de arquivos com compressão gzip.
Mais informações: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Alterar compressão de um arquivo compactado com compressão gzip:

`gzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>

- Descompactar arquivo gzip definindo arquivo final:

`gzip -c -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>`.gz > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_descompactado.ext</span>

- Compactar arquivo definindo arquivo final:

`gzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.ext.gz</span>

- Compactando arquivos em gzip definindo o nível de compressão [9]:

`gzip -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.ext</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_compactado.ext.gz</span>
