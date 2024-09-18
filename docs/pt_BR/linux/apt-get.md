---
layout: page
title: linux/apt-get (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em Debian."
content_hash: 98fc56926591d7ce6626cc2cf3358f1cad4ce0cf
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Gerenciador de pacotes das distribuições baseadas em Debian.
Procure por pacotes utilizando o `apt-cache`.
Mais informações: <https://manned.org/apt-get.8>.

- Atualiza a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt-get`):

`apt-get update`

- Instala um pacote ou atualizá-lo para a versão mais recente:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remove um pacote e os seus arquivos de configuração:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Atualiza todos os pacotes instalados para as versões mais recentes:

`apt-get upgrade`

- Limpa o repositório local — removendo os arquivos de pacotes (`.deb`) de downloads interrompidos que não podem mais ser baixados:

`apt-get autoclean`

- Remove todos os pacotes obsoletos:

`apt-get autoremove`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`apt-get dist-upgrade`
