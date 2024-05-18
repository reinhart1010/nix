---
layout: page
title: common/archwiki-rs (español)
description: "Lee, busca y descarga páginas de la ArchWiki."
content_hash: 29c50ad963285131e3fbed783d31a6af07d10a18
last_modified_at: 2024-05-18
related_topics:
  - title: English version
    url: /en/common/archwiki-rs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# archwiki-rs

Lee, busca y descarga páginas de la ArchWiki.
Más información: <https://gitlab.com/lucifayr/archwiki-rs>.

- Lee una página de la ArchWiki:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_de_página</span>

- Lee una página de la ArchWiki en el formato especificado:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_de_página</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>

- Busca páginas en ArchWiki con el texto proporcionado:

`archwiki-rs search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_a_buscar</span>`" --text-search`

- Descarga una copia local de todas las páginas de ArchWiki en un directorio específico:

`archwiki-rs local-wiki `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/wiki_local</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>
