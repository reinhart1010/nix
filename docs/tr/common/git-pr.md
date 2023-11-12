---
layout: page
title: common/git-pr (Türkçe)
description: "Github çekme isteklerini (pr) yerelde kontrol et."
content_hash: 514cb6a11f33747203164cc740beaa706529cff8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-pr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git pr

Github çekme isteklerini (pr) yerelde kontrol et.
Daha fazla bilgi için: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Belirtilen çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_numarası</span>

- Belirtilen dış bağlantıdan gelen bir çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_numarası</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dış_bağlantı</span>

- Belirtilen URL'den gelen çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Eski çekme isteği dallarını temizle:

`git pr clean`
