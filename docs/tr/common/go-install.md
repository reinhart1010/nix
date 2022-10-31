---
layout: page
title: common/go-install (Türkçe)
description: "İçe aktarım yollarıyla isimlendirilen paketleri derle ve indir."
content_hash: cb63d1ac004c11a9c76efe67c8e011d4b4e883e9
related_topics:
  - title: English version
    url: /en/common/go-install.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># go install

İçe aktarım yollarıyla isimlendirilen paketleri derle ve indir.
Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Mevcut paketi derle ve indir:

`go install`

- Belirtilen yerel paketi derle ve indir:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/konum/paket</span>

- Bir programın son sürümünü mevcut dizindeki `go.mod`'u yoksayarak indir:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>

- Bir programın mevcut dizindeki `go.mod`'da belirtilen sürümünü indir:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>
