---
layout: page
title: linux/aptitude (português (Brasil))
description: "Utilitário de gerenciamento de pacotes de Debian e Ubuntu."
content_hash: 5a7070f149b63b5b0ceb56215cbaa334e8a5a115
last_modified_at: 2024-10-03
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aptitude.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aptitude

Utilitário de gerenciamento de pacotes de Debian e Ubuntu.
Mais informações: <https://manned.org/aptitude.8>.

- Sincroniza a lista de pacotes e versões disponíveis. Deve ser executado antes de outros comandos `aptitude`:

`aptitude update`

- Instala um novo pacote e suas dependências:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Busca por um determinado pacote:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Busca por uma determinado pacote instalado (`?installed` é um termo de busca `aptitude`):

`aptitude search '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`)'`

- Remove um pacote e todos que dependam dele:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Atualiza os pacotes instalados para suas versões mais recentes:

`aptitude upgrade`

- Atualiza os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`

- Coloca um pacote instalado em espera para prevenir atualizações automáticas:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>`)'`
