---
layout: page
title: linux/chattr (português (Brasil))
description: "Altera os atributos de arquivos ou diretórios."
content_hash: a39714530bf30ae2d6128ffb7e99f7b82e5db03b
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/chattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chattr

Altera os atributos de arquivos ou diretórios.
Mais informações: <https://manned.org/chattr>.

- Bloqueia um arquivo ou diretório para mudanças ou remoção, mesmo para um super usuário:

`chattr +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_arquivo_ou_diretorio</span>

- Desbloqueia um arquivo ou diretório:

`chattr -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_arquivo_ou_diretorio</span>

- Bloqueia diretório e todos os seus arquivos para mudanças ou remoção:

`chattr -R +i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_do_diretorio</span>
