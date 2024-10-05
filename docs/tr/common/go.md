---
layout: page
title: common/go (Türkçe)
description: "Go kaynak kodunu yönetmeye yarayan bir araç."
content_hash: dcddf8c1bbf704746fc63ea59860a61744e9a192
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/go.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go

Go kaynak kodunu yönetmeye yarayan bir araç.
`build` gibi bazı alt komutların kendı kullanım dokümentasyonları mevcut.
Daha fazla bilgi için: <https://golang.org>.

- İçe aktarım yolunda belirtilen şekilde bir paketi indir ve yükle:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_yolu</span>

- Bir kaynak dosyasını derle ve çalıştır (bir `main` paketine sahip olmalı):

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya</span>`.go`

- Bir kaynak dosyasını belirtilen çalıştırılabilir dosyaya derle:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">çalıştırılabilir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya</span>`.go`

- Mevcut dizinde bulunan paketi derle:

`go build`

- Mevcut paket için tüm test durumlarını çalıştır (bahsi geçen dosyalar `_test.go` ifadesi ile bitmeli):

`go test`

- Mevcut paketi derle ve indir:

`go install`

- Mevcut diizinde yeni bir modül başlat:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modül_ismi</span>
