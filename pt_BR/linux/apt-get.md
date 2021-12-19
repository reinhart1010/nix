---
layout: page
title: linux/apt-get (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em Debian."
content_hash: f8f06b912f16967f12b60eb87f8a17d3e2d64bba
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
---
# apt-get

Gerenciador de pacotes das distribuições baseadas em Debian.
Procure por pacotes utilizando o `apt-cache`.
Mais informações: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Atualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `apt-get`):

`apt-get update`

- Instalar um pacote ou atualizá-lo para a versão mais recente:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remover um pacote:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Remover um pacote e os seus arquivos de configuração:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Atualizar todos os pacotes instalados para as versões mais recentes:

`apt-get upgrade`

- Limpar o repositório local — removendo os arquivos de pacotes (`.deb`) de downloads interrompidos que não podem mais ser baixados:

`apt-get autoclean`

- Remover todos os pacotes obsoletos:

`apt-get autoremove`

- Atualizar os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`apt-get dist-upgrade`
