---
layout: page
title: common/git-subtree (Türkçe)
description: "Proje bağımlılıklarını alt proje olarak yönetmeye yarayan bir araç."
content_hash: e23994d990fbdbeaf98a230af65879b82603d13d
related_topics:
  - title: English version
    url: /en/common/git-subtree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-subtree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-subtree.html
    icon: bi bi-globe
---
# git subtree

Proje bağımlılıklarını alt proje olarak yönetmeye yarayan bir araç.
Daha fazla bilgi: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Bir Git deposunu alt ağaç olarak ekle:

`git subtree add --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>` --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Alt ağaç deposunu son commit'ine güncelle:

`git subtree pull --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Son alt ağaca kadar olan değişiklikleri alt ağaca commit'le:

`git subtree merge --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>`} --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Commit'leri bir alt ağaç deposuna yolla:

`git subtree push --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>`} `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Bir alt ağacın geçmişinden yeni bir proje geçmişi dışa aktar:

`git subtree split --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dizin/konumu</span>`} `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">depo_url'si</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>
