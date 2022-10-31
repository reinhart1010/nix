---
layout: page
title: common/go-fmt (Türkçe)
description: "Go kaynak dosyalarını formatla."
content_hash: 4c3e9ab709d658f7817621965645030dca5aa251
related_topics:
  - title: English version
    url: /en/common/go-fmt.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go fmt

Go kaynak dosyalarını formatla.
Değiştirilen dosya isimlerini yazdırır.
Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- Mevcut dizindeki Go kaynak dosyalarını formatla:

`go fmt`

- Belirtilen Go paketini içe aktarım yolunda formatla (`$GOPATH/src`):

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/paket</span>

- Paketi mevcut dizinde ve tüm öbür alt dizinlerde formatla (`...` ifadesine dikkat):

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./...</span>

- Hiçbir şeyi düzenlemeden format komutlarının ne yapacağını yazdır:

`go fmt -n`

- Komut çalışırken arkaplanda hangi komutların çalıştığını yazdır:

`go fmt -x`
