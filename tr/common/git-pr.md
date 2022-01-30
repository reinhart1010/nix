---
layout: page
title: common/git-pr (Türkçe)
description: "Github çekme isteklerini (pr) yerelde kontrol et."
content_hash: 9e141948dd9cae0803e990c5f13eee72f39b93f4
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
---
# git pr

Github çekme isteklerini (pr) yerelde kontrol et.
Daha fazla bilgi: <https://github.com/tj/git-extras/blob/master/Commands.md#git-pr>.

- Belirtilen çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_numarası</span>

- Belirtilen dış bağlantıdan gelen bir çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_numarası</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dış_bağlantı</span>

- Belirtilen URL'den gelen çekme isteğini kontrol et:

`git pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Eski çekme isteği dallarını temizle:

`git pr clean`
