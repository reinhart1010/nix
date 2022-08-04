---
layout: page
title: linux/chattr (português (Brasil))
description: "Altera os atributos de arquivos ou diretórios."
content_hash: 3312670277bbfc8d80ab803a3f7b5a0ae790228a
related_topics:
  - title: English version
    url: /en/linux/chattr.html
    icon: bi bi-globe
---
# chattr

Altera os atributos de arquivos ou diretórios.
Mais informações: <https://manned.org/chattr>.

- Bloquear um arquivo ou diretório para mudanças ou remoção, mesmo para um super usuário:

`chattr +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_arquivo_ou_diretorio</span>

- Desbloquear um arquivo ou diretório:

`chattr -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_arquivo_ou_diretorio</span>

- Bloquear diretório e todos os seus arquivos para mudanças ou remoção:

`chattr -R +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_diretorio</span>
