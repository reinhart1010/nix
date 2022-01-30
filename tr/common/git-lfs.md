---
layout: page
title: common/git-lfs (Türkçe)
description: "Git depolarındaki büyük dosyalarla çalış."
content_hash: ce99f4a3cde9021a179c6f6a00ad149f38fa3bf6
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
---
# git lfs

Git depolarındaki büyük dosyalarla çalış.
Daha fazla bilgi: <https://git-lfs.github.com>.

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
