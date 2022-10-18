---
layout: page
title: common/git-check-attr (Türkçe)
description: "`gitattributes` içeriği görüntüleme aracı."
content_hash: bf4b550410e0b0a36c0e7ffff4b692555b88ca7b
related_topics:
  - title: English version
    url: /en/common/git-check-attr.html
    icon: bi bi-globe
---
# git check-attr

`gitattributes` içeriği görüntüleme aracı.
Daha fazla bilgi: <https://git-scm.com/docs/git-check-attr>.

- Bir dosyadaki tüm atıfları kontrol et:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Bir dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atıf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya2</span>

- Bir veya birden fazla dosyadaki belirtilmiş atıfın değerini kontrol et:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atıf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya2</span>
