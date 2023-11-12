---
layout: page
title: common/git-replace (Türkçe)
description: "Nesnelerin yerini değiştirmek için referans oluştur, sırala ve sil."
content_hash: 0f9b0d2a92d188299f7ca1cf397da15ad10fe33f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-replace.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-replace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git replace

Nesnelerin yerini değiştirmek için referans oluştur, sırala ve sil.
Daha fazla bilgi için: <https://git-scm.com/docs/git-replace>.

- Öbür commit'lere dokunmadan bir commit'in başka bir commit ile yerini değiştir:

`git replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yer_değiştirme</span>

- Belirtilen nesnede varolan yer değiştirme referanslarını sil:

`git replace --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>

- Bir nesnenin içeriğini etkileşimli olarak düzenle:

`git replace --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nesne</span>
