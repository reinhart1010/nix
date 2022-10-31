---
layout: page
title: common/go-build (Türkçe)
description: "Go kaynaklarını derle."
content_hash: d6753b8021b51eb90fbe4d740d3d2ba9abc62bf1
related_topics:
  - title: English version
    url: /en/common/go-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-build.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go build

Go kaynaklarını derle.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Bir 'package main' dosyasını derle (çıktı uzantısız bir dosya ismi olacak):

`go build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/main.go</span>

- Çıktı dosya ismini belirterek derle:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/kaynak.go</span>

- Bir paket yarat:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/paket</span>

- Bir ana paketi veri yarış tanımlayıcısını etkinleştirerek çalıştırılabilir olarak derle.

`go build -race -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/çalıştırılabilir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/ana_paket</span>
