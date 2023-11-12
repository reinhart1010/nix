---
layout: page
title: common/go-build (Türkçe)
description: "Go kaynaklarını derle."
content_hash: bf39908084b05cf9b1bce8bfaff70070c117b7b4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go build

Go kaynaklarını derle.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Bir 'package main' dosyasını derle (çıktı uzantısız bir dosya ismi olacak):

`go build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/main.go</span>

- Çıktı dosya ismini belirterek derle:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/kaynak.go</span>

- Bir paket yarat:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/paket</span>

- Bir ana paketi veri yarış tanımlayıcısını etkinleştirerek çalıştırılabilir olarak derle:

`go build -race -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/çalıştırılabilir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/ana_paket</span>
