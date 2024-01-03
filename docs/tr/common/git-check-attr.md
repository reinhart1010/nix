---
layout: page
title: common/git-check-attr (Türkçe)
description: "`gitattributes` içeriği görüntüleme aracı."
content_hash: 9a250cf36afa1fa1b4fda8c1ef3a77923b3b94f1
last_modified_at: 2024-01-03
related_topics:
  - title: English version
    url: /en/common/git-check-attr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-attr

`gitattributes` içeriği görüntüleme aracı.
Daha fazla bilgi için: <https://git-scm.com/docs/git-check-attr>.

- Bir dosyadaki tüm atıfları kontrol et:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Bir dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atıf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya1 örnek/dosya2 ...</span>

- Bir veya birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atıf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya1 örnek/dosya2 ...</span>
