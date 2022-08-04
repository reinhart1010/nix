---
layout: page
title: common/git-svn (Türkçe)
description: "Bir alt sürüm deposu ve Git arasında çift yönlü operasyon."
content_hash: 8ec675fe576823a9ffefe07729bdcf5a2a0f3bfe
related_topics:
  - title: English version
    url: /en/common/git-svn.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-svn.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-svn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-svn.html
    icon: bi bi-globe
---
# git svn

Bir alt sürüm deposu ve Git arasında çift yönlü operasyon.
Daha fazla bilgi: <https://git-scm.com/docs/git-svn>.

- Bit SVN deposunu klonla:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ornek.com/altsürüm_deposu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yerel_dizin</span>

- Bir SVN deposunu belirtilen düzenleme numarasından başlayarak klonla:

`git svn clone -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.ornek.net/altsürüm/depo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yerel_dizin</span>

- Uzak SVN deposundan yerel klonu güncelle:

`git svn rebase`

- Git HEAD'i değiştirmeden uzak SVN deposundan güncellemeleri çek:

`git svn fetch`

- SVN deposuna geri commit'le:

`git svn dcommit`
