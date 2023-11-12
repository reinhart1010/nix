---
layout: page
title: common/go-mod (Türkçe)
description: "Modül yönetimi."
content_hash: fa123d3267e7c36e6d54f91b47181488ab291215
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-mod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go mod

Modül yönetimi.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- Mevcut dizinde yeni modül başlat:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modülİsmi</span>

- Modülleri yerel önbelleğe yükle:

`go mod download`

- Kaybolan modülleri ekle ve kullanılmayanları sil:

`go mod tidy`

- Bağlılıkların beklenen içeriğe sahip olduklarını doğrula:

`go mod verify`

- Tüm bağlılıkların kaynaklarını satıcı dizine kopyala:

`go mod vendor`
