---
layout: page
title: common/git-annex (Türkçe)
description: "Git ile dosyaları, dosyaların içeriğine bakmadan yönet."
content_hash: 9a191493288ace616024cd010f242e3fba617c62
related_topics:
  - title: English version
    url: /en/common/git-annex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-annex.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-annex.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git annex

Git ile dosyaları, dosyaların içeriğine bakmadan yönet.
Daha fazla bilgi için:<https://git-annex.branchable.com>.

- Yardım:

`git annex help`

- Git annex ile bir depo başlat:

`git annex init`

- Bir dosya ekle:

`git annex add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>

- Bir dosya veya dizinin şu anki durumunu göster:

`git annex status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>

- Yerel bir depoyu, uzaktaki bir depo ile senkronize et:

`git annex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı</span>

- Bir dosya veya dizin al:

`git annex get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya_veya_dizin</span>
