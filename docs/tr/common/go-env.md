---
layout: page
title: common/go-env (Türkçe)
description: "Go toolchain'in kullandığı ortam değişkenlerini yönet."
content_hash: f37535f44d4f259df5fe6b23489968917a122a7c
related_topics:
  - title: English version
    url: /en/common/go-env.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-env.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go env

Go toolchain'in kullandığı ortam değişkenlerini yönet.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Tüm ortam değişkenlerini göster:

`go env`

- Belirtilen ortam değişkenlerini göster:

`go env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOPATH</span>

- Bir değere ortam değişkeni ata:

`go env -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/dizin</span>

- Ortam değişkeninin değerini sıfırla:

`go env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>
