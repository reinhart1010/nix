---
layout: page
title: common/git-lfs (Türkçe)
description: "Git depolarındaki büyük dosyalarla çalış."
content_hash: edb4da9ec0ace85de5af29dfc35408e88b52ea7d
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-lfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-lfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-lfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-lfs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-lfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git lfs

Git depolarındaki büyük dosyalarla çalış.
Daha fazla bilgi için: <https://git-lfs.com>.

- Git LFS'i başlat:

`git lfs install`

- Belirtilen topağa uygun dosyaları izle:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Git LFS uç nokta URL'sini değiştir (LFS sunucusunun Git sunucusundan ayrı olması durumunda işlevseldir):

`git config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--file</span>` .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_uç_nokta_url'si</span>

- İzlenen kalıpları sırala:

`git lfs track`

- Commit'lenmiş izlenen dosyaları sırala:

`git lfs ls-files`

- Tğm Git LFS nesnelerini uzak sunucuya gönder (hatayla karşılaşma durumunda faydalıdır):

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_depo_adresi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Tüm Git LFS nesnelerini çek:

`git lfs fetch`

- Tüm Git LFS nesnelerini kontrol et:

`git lfs checkout`
