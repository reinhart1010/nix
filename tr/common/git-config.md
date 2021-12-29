---
layout: page
title: common/git-config (Türkçe)
description: "Git depoları için yazılan kişisel konfigürasyon seçeneklerini yönet."
content_hash: f71fc445b994db5052095a2d9758d62401315ca7
related_topics:
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-config.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git config

Git depoları için yazılan kişisel konfigürasyon seçeneklerini yönet.
Bu konfigürasyonlar lokal (mevcut depo için) veya evrensel (mevcut kullanıcı için) olabilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-config>.

- Yalnızca (mevcut depodaki `.git/config`'de saklanan) yerel konfigürasyon kayıtlarını sırala:

`git config --list --local`

- Yalnızca (bilgisayardaki `~/.gitconfig`'de saklanan) evrensel konfigürasyon kayıtlarını sırala:

`git config --list --global`

- Yerel veya evrensel olarak tanımlanan tüm konfigürasyon kayıtlarını sırala:

`git config --list`

- Belirtilen bir konfigürasyon kaydının değerini öğren:

`git config alias.unstage`

- Belirtilen bir konfigürasyon kaydının evrensel değerini belirle:

`git config --global alias.unstage "reset HEAD --"`

- Evrensel bir konfigürasyon kaydını varsayılan değerine geri al:

`git config --global --unset alias.unstage`

- Mevcut depodaki Git konfigürasyonunu varsayılan metin düzenleyici ile düzenle:

`git config --edit`

- Evrensel Git konfigürasyonunu varsayılan metin düzenleyici ile düzenle:

`git config --global --edit`
