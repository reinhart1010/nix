---
layout: page
title: common/ftp (português (Brasil))
description: "Ferramentas para interagir com um servidor via Protocolo de Transferência de Arquivos."
content_hash: 6009b102b4f392de901696da4138a5d09a157808
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ftp.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ftp

Ferramentas para interagir com um servidor via Protocolo de Transferência de Arquivos.
Mais informações: <https://manned.org/ftp>.

- Conecta-se a um servidor FTP:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.exemplo.com</span>

- Alterna para o modo de transferência binária (gráficos, arquivos compactados, etc):

`binary`

- Transfere vários arquivos sem solicitar confirmação em cada arquivo:

`prompt off`

- Baixa vários arquivos (expressão glob):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Carrega vários arquivos (expressão glob):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Exclui vários arquivos no servidor remoto:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Renomeia um arquivo no servidor remoto:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo_original</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_novo_arquivo</span>
