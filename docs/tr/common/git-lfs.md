---
layout: page
title: common/git-lfs (Türkçe)
description: "Git depolarındaki büyük dosyalarla çalış."
content_hash: 825fb39ef6a22bf7537b423e915f716332c4a574
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# git lfs

Git depolarındaki büyük dosyalarla çalış.
Daha fazla bilgi için: <https://git-lfs.github.com>.

- Git LFS'i başlat:

`git lfs install`

- Belirtilen topağa uygun dosyaları izle:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Git LFS uç nokta URL'sini değiştir (LFS sunucusunun Git sunucusundan ayrı olması durumunda işlevseldir):

`git config -f .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_uç_nokta_url'si</span>

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
