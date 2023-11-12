---
layout: page
title: common/go-get (Türkçe)
description: "Bir bağımlılık paketi ekle veya eski GOPATH modunda paket indir."
content_hash: b15d8ab58ddefbec7665441daf308df1c0fc350b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go get

Bir bağımlılık paketi ekle veya eski GOPATH modunda paket indir.
Daha fazla bilgi için: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- `go.mod`'a modül modunda (module-mode) belirtilen bir paket ekle veya paketi GOPATH modunda indir:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ornek.com/pkg</span>

- Paketi module-aware modunda belirtilen sürümde düzenle:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ornek.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.2.3</span>

- Belirtilen paketi sil:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ornek.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>
