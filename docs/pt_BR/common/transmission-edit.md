---
layout: page
title: common/transmission-edit (português (Brasil))
description: "Modifica URLs de anúncio a partir de arquivos de torrent."
content_hash: bc46682a4269f1d4b2c412c4ceb999eafac9daa8
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/transmission-edit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-edit

Modifica URLs de anúncio a partir de arquivos de torrent.
Veja também: `transmission`.
Mais informações: <https://manned.org/transmission-edit>.

- Adiciona ou remove uma URL a partir da lista de anúncio do torrent:

`transmission-edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://exemplo.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.torrent</span>

- Atualiza um código do rastreador em um arquivo de torrent:

`transmission-edit --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antigo-código</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo-código</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.torrent</span>
