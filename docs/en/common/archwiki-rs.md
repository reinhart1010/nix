---
layout: page
title: common/archwiki-rs (English)
description: "Read, search and download pages from the ArchWiki."
content_hash: 862aa71316f3b260a0a3f87621ef71def12b33c6
last_modified_at: 2024-05-02
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/archwiki-rs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># archwiki-rs

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
