---
layout: page
title: common/git-submodule (Türkçe)
description: "Alt modülleri incele, güncelle ve yönet."
content_hash: bd1c68734686a3e366829e586bb50f2ff5f32ee7
related_topics:
  - title: English version
    url: /en/common/git-submodule.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-submodule.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-submodule.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-submodule.html
    icon: bi bi-globe
---
# git submodule

Alt modülleri incele, güncelle ve yönet.
Daha fazla bilgi için: <https://git-scm.com/docs/git-submodule>.

- Deponun belirtilen alt modüllerini indir:

`git submodule update --init --recursive`

- Bir Git deposunu alt modül olarak ekle:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>

- Bir Git deposunu alt modül olarak belirtilen dizinde ekle:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>

- Tüm alt modülleri son commit'lerine güncelle:

`git submodule foreach git pull`
