---
layout: page
title: common/git-prune (Türkçe)
description: "Nesne veritabanından erişilemeyen tüm nesneleri budamaya yarayan git komutu."
content_hash: 5af517af3d436075919611423e92b50e66ce5f54
related_topics:
  - title: English version
    url: /en/common/git-prune.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-prune.html
    icon: bi bi-globe
---
# git prune

Nesne veritabanından erişilemeyen tüm nesneleri budamaya yarayan git komutu.
Bu komut genelde doğrudan kullanılmasa da Git gc tarafından bir iç komut olarak kullanılmaktadır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-prune>.

- Git prune tarafından silinebilecek nesneleri onları silmeden raporla:

`git prune --dry-run`

- Erişilemeyen nesneleri buda ve stdout'a budanan şeyleri görüntüle:

`git prune --verbose`

- Erişilemeyen nesneleri budarken ilerlemeyi göster:

`git prune --progress`
