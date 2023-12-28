---
layout: page
title: linux/dpkg (português (Brasil))
description: "Gerenciador de pacotes Debian."
content_hash: 9caf166879997f1ba128635b4339ec47beecbb39
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/linux/dpkg.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dpkg.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/dpkg.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dpkg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg

Gerenciador de pacotes Debian.
Alguns subcomandos como `dpkg deb` tem sua própia documentação de uso.
Mais informações: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Instala um pacote:

`dpkg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.deb</span>

- Remove um pacote:

`dpkg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe os pacotes correspondentes ao critério de busca:

`dpkg -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Exibe o conteúdo do pacote:

`dpkg -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Exibe o conteúdo do arquivo de um pacote:

`dpkg -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.deb</span>

- Apresenta o pacote proprietário de um determinado arquivo:

`dpkg -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>
