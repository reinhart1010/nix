---
layout: page
title: common/buku (English)
description: "Command-line browser-independent bookmark manager."
content_hash: 4b11bd5aa7624d5b6d15704711a6726f12ab7e4d
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/buku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# buku

Command-line browser-independent bookmark manager.
More information: <https://github.com/jarun/Buku>.

- Display all bookmarks matching "keyword" and with "privacy" tag:

`buku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyword</span>` --stag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">privacy</span>

- Add bookmark with tags "search engine" and "privacy":

`buku --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search engine</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">privacy</span>

- Delete a bookmark:

`buku --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark_id</span>

- Open editor to edit a bookmark:

`buku --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark_id</span>

- Remove "search engine" tag from a bookmark:

`buku --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bookmark_id</span>` --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search engine</span>
