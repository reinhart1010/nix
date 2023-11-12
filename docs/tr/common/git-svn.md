---
layout: page
title: common/git-svn (Türkçe)
description: "Bir alt sürüm deposu ve Git arasında çift yönlü operasyon."
content_hash: cfc7b2cfb6166e17bbe13137c266b72d53da5301
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# git svn

Bir alt sürüm deposu ve Git arasında çift yönlü operasyon.
Daha fazla bilgi için: <https://git-scm.com/docs/git-svn>.

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
