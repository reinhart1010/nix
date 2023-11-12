---
layout: page
title: common/jar (português (Brasil))
description: "Compactador de Bibliotecas e Aplicações Java."
content_hash: 1d99786a593c0db788c8caa55d768bafc1c5eb44
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/jar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/jar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jar

Compactador de Bibliotecas e Aplicações Java.
Mais informações: <https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- Arquiva recursivamente todos os arquivos do diretório atual em um arquivo .jar:

`jar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.jar</span>` *`

- Descompacta o arquivo .jar/.war para o diretório atual:

`jar -xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.jar</span>

- Lista o conteúdo do arquivo .jar/.war:

`jar tf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.jar</span>

- Lista o conteúdo do arquivo .jar/.war com mais detalhes (verbose):

`jar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.jar</span>
