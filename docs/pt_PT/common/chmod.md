---
layout: page
title: common/chmod (português (Portugal))
description: "Alterar as permissões de acesso a um ficheiro ou diretório."
content_hash: 3b52a05522a886a15a348a63e0916ad71d50cbcc
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
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chmod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chmod

Alterar as permissões de acesso a um ficheiro ou diretório.
Mais informações: <https://www.gnu.org/software/coreutils/chmod>.

- Dar a um [u]tilizador que possui um ficheiro o direito a e[x]ecutá-lo:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Dar a um [u]tilizador direitos para le[r] e escrever ([w]) num ficheiro/diretório:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro_ou_diretorio</span>

- Remover direitos de execução de um [g]rupo:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Dar a todos ([a]) os utilizadores o direito de le[r] e e[x]ecutar:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Dar a [o]utros (que não estão no grupo do dono do ficheiro) os mesmos direitos do [g]rupo:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Remover todos os direitos dos [o]utros:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ficheiro</span>

- Mudar as permissões, recursivamente, dando ao [g]rupo e [o]utros a possibilidade de escrever ([w]):

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diretorio</span>
