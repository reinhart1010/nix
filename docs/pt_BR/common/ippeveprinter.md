---
layout: page
title: common/ippeveprinter (português (Brasil))
description: "Um servidor de impressão IPP Everywhere simples."
content_hash: ede9380f986dfd912cba1354ee98e6b1582eceab
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/ippeveprinter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ippeveprinter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ippeveprinter

Um servidor de impressão IPP Everywhere simples.
Veja também: `ippeveps`, `ippevepcl`.
Mais informações: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>.

- Executa o servidor com um nome de serviço específico:

`ippeveprinter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`

- Carrega os atributos da impressora de um arquivo PPD:

`ippeveprinter -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ppd</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`

- Executa o comando `file` sempre que um trabalho é enviado para o servidor:

`ippeveprinter -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/file</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`

- Especifica o diretório que vai conter os arquivos de impressão (por padrão, um diretório dentro do diretório temporário do usuário):

`ippeveprinter -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretório_spool</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`

- Mantém os documentos de impressão no diretório de spool em vez de exclui-los:

`ippeveprinter -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`

- Especifica a velocidade da impressora na unidade páginas/minuto (10 por padrão):

`ippeveprinter -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocidade</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_serviço</span>`"`
