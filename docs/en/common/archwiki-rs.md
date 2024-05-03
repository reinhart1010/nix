---
layout: page
title: common/archwiki-rs (English)
description: "Read, search and download pages from the ArchWiki."
content_hash: 862aa71316f3b260a0a3f87621ef71def12b33c6
last_modified_at: 2024-05-03
tldri18n_status: 2
---
# archwiki-rs

Read, search and download pages from the ArchWiki.
More information: <https://gitlab.com/lucifayr/archwiki-rs>.

- Read a page from the ArchWiki:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_title</span>

- Read a page from the ArchWiki in the specified format:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page_title</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>

- Search the ArchWiki for pages containing the provided text:

`archwiki-rs search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_text</span>`" --text-search`

- Download a local copy of all ArchWiki pages into a specific directory:

`archwiki-rs local-wiki `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/local_wiki</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>
