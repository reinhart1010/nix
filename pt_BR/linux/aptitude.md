---
layout: page
title: linux/aptitude (português (Brasil))
description: "Gerenciador de pacotes das distribuições baseadas em Debian."
content_hash: 4bf01adba71060de090e5710ea333810f9ba1d2f
related_topics:
  - title: Deutsch version
    url: /de/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aptitude.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aptitude

Gerenciador de pacotes das distribuições baseadas em Debian.
Mais informações: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Atualizar a lista de pacotes disponíveis (recomenda-se executá-lo antes de outros comandos `aptitude`):

`aptitude update`

- Instalar um novo pacote e suas dependências:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Buscar pacotes correspondentes ao critério de busca:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">criterio_de_busca</span>

- Remover um pacote e todos que dependam dele:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Atualizar os pacotes instalados para as versões mais recentes:

`aptitude upgrade`

- Atualizar os pacotes instalados (semelhante ao `upgrade`), porém removendo os obsoletos e instalando pacotes solicitados por novas dependências:

`aptitude full-upgrade`
