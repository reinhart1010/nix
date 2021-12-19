---
layout: page
title: linux/dpkg (português (Brasil))
description: "Gerenciador de pacotes Debian."
content_hash: bbb247360432d0c4ec7d7bc50e05e3ad597849d0
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
---
# dpkg

Gerenciador de pacotes Debian.
Alguns subcomandos como `dpkg deb` tem sua própia documentação de uso.
Mais informações: <https://manpages.debian.org/buster/dpkg/dpkg.1.en.html>.

- Instalar um pacote:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.deb</span>

- Remover um pacote:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibir os pacotes correspondentes ao critério de busca:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Exibe o conteúdo do pacote:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibir o conteúdo do arquivo de um pacote:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.deb</span>

- Apresentar o pacote proprietário de um determinado arquivo:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>
