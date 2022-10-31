---
layout: page
title: common/go-test (Türkçe)
description: "Go paketlerini test et (dosyalar `_test.go` ifadesiyle bitmeli)."
content_hash: 946d5a96bc03e0a38f7b503b0e81cafcb7274271
related_topics:
  - title: English version
    url: /en/common/go-test.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go test

Go paketlerini test et (dosyalar `_test.go` ifadesiyle bitmeli).
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Testing_flags>.

- Mevcut dizinde bulunan paketleri test et:

`go test`

- Mevcut dizindeki paketleri ayrıntılı şekilde test et:

`go test -v`

- Mevcut dizindeki ve tüm alt dizinlerdeki paketleri test et (`...` ifadesine dikkat):

`go test -v ./...`

- Mevcut dzindeki paketleri test et ve tüm kalite testlerini çalıştır:

`go test -v -bench .`

- Mevcut dizindeki paketleri test et ve 50 saniye içinde tüm kalite testlerini çalıştır:

`go test -v -bench . -benchtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50s</span>

- Paketleri kapsamlı bir analiz ile test et:

`go test -cover`
