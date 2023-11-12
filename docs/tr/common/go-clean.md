---
layout: page
title: common/go-clean (Türkçe)
description: "Obje ve önbellek dosyalarını sil."
content_hash: 9a7de61b9ce8735b5f5e826c5f17479ba48e8a05
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/go-clean.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go clean

Obje ve önbellek dosyalarını sil.
Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Remove_object_files_and_cached_files>.

- Hiçbir şeyi silmeden silme komutlarını yazdır:

`go clean -n`

- Yapım önbelleğini sil:Delete the build cache:

`go clean -cache`

- Tüm önbelleğe alınan test sonuçlarını sil:

`go clean -testcache`

- Modül önbelleğni sil:

`go clean -modcache`
