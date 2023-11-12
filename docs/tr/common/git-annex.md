---
layout: page
title: common/git-annex (Türkçe)
description: "Git ile dosyaları, dosyaların içeriğine bakmadan yönet."
content_hash: 0721a0cb7bfea3da9e446a2f563c1490e320af9f
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# git annex

Git ile dosyaları, dosyaların içeriğine bakmadan yönet.
Daha fazla bilgi için: <https://git-annex.branchable.com>.

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

- Yardım görüntüle:

`git annex help`
