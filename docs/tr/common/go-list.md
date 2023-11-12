---
layout: page
title: common/go-list (Türkçe)
description: "Paket ve modülleri sırala."
content_hash: d8625be08e8f8bb1f792b38f38cf3b48bcdc6d9e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go list

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
