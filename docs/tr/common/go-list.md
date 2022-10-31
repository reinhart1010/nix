---
layout: page
title: common/go-list (Türkçe)
description: "Paket ve modülleri sırala."
content_hash: d8625be08e8f8bb1f792b38f38cf3b48bcdc6d9e
related_topics:
  - title: English version
    url: /en/common/go-list.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go list

Paket ve modülleri sırala.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-List_packages_or_modules>.

- Paketleri sırala:

`go list ./...`

- Standart paketleri sırala:

`go list std`

- Paketleri JSON formatında sırala:

`go list -json time net/http`

- Modül bağımlılıklarını ve erişilebilir güncellemeleri sırala:

`go list -m -u all`
