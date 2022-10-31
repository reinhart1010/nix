---
layout: page
title: common/go-tool (Türkçe)
description: "Belirtilen bir Go aracını veya komutunu çalıştır."
content_hash: 7fb7cd1e73b713bd475d225bee00d342116cd80e
related_topics:
  - title: English version
    url: /en/common/go-tool.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go tool

Belirtilen bir Go aracını veya komutunu çalıştır.
Bir Go komutunu tipik olarak hata ayıklamak için tek başına bir binary olarak çalıştır.
Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Run_specified_go_tool>.

- Erişilebilir araçları sırala:

`go tool`

- Go bağ aracını çalıştır:

`go tool link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/main.o</span>

- Çalıştırılacak komutu çalıştırmadan yazdır (`whereis`'e benzer):

`go tool -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argümanları</span>

- Belirtilen araç için resmi dokümentasyonu göster:

`go tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komut</span>` --help`
