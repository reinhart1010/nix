---
layout: page
title: common/chmod (português (Brasil))
description: "Muda a permissão de acesso de um arquivo ou diretório."
content_hash: c324390a5b856ec41d2d5c6ed15dff62148d4083
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
---
# chmod

Muda a permissão de acesso de um arquivo ou diretório.
Mais informações: <https://www.gnu.org/software/coreutils/chmod>.

- Dá ao [u]suário dono de um arquivo o direito de e[x]ecutá-lo:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Dá ao [u]suário direitos para le[r] e [w]escrever em um arquivo/diretório:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo_ou_diretorio</span>

- Remove direitos e[x]ecutáveis de um [g]rupo:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Dá a [a]todos os usuários direitos para le[r] e e[x]ecutar:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Dá para [o]utros (que não estejam no grupo do proprietário do arquivo) os mesmos direitos que o [g]rupo:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Remove todos os direitos de [o]utros:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Muda recursivamente as permissões, dando para [g]rupo e [o]utros a habilidade para [w]escrever:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretorio</span>

- Recursivamente concede a [a]todos os usuários permissões de leitu[r]a para arquivos e e[X]ecute permissões para sub-diretórios dentro de um diretório:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretorio</span>
