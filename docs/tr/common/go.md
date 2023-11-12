---
layout: page
title: common/go (Türkçe)
description: "Go kaynak kodunu yönetmeye yarayan bir araç."
content_hash: e25e1c1fdb16875eb0a6b9ef7c3d493bcf9d35f6
last_modified_at: 2023-11-12
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
`go build` gibi bazı alt komutların kendı kullanım dokümentasyonları mevcut.
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
