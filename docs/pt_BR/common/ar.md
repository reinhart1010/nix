---
layout: page
title: common/ar (português (Brasil))
description: "Cria, modifica e extrai de arquivos Unix. Normalmente usado para bibliotecas estáticas (`.a`) e pacotes Debian (`.deb`)."
content_hash: b2ef8c46208175f79f513a12edab188842af248a
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

Cria, modifica e extrai de arquivos Unix. Normalmente usado para bibliotecas estáticas (`.a`) e pacotes Debian (`.deb`).
Veja também: `tar`.
Mais informações: <https://manned.org/ar>.

- Descompacta todos os membros de um arquivo compactado:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.a</span>

- Lista o conteúdo em um arquivo compactado específico:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.ar</span>

- Substitui ou adiciona arquivos específicos para um arquivo compactado:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/binário-debian caminho/para/control.tar.gz caminho/para/data.tar.xz ...</span>

- Insere um índice de arquivos objetos (equivalente a usar `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.a</span>

- Cria um arquivo compactado com arquivos específicos, acompanhado por um índice de arquivo objeto:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1.o caminho/para/arquivo2.o ...</span>
