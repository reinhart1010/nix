---
layout: page
title: common/git-rebase (Türkçe)
description: "Bir daldan başka bir dalın üstüne commit'leri tekrar temeller."
content_hash: c38be3621a295a316d6089a64c8afa3e7dc820dd
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Bir daldan başka bir dalın üstüne commit'leri tekrar temeller.
Sıklıkla bir dalı commit'leriyle beraber başka bir tabana "taşımak" için kullanılır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-rebase>.

- Mevcut dalı belirtilen öbür dal üzerine temelle:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_taban_dal</span>

- Commit'lerin sıralanması, çıkartılması, birleştirilmesi veya modifiye edilmesine izin vermek için tekrar temellemeyi etkileşimli olacak şekilde başlat:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hedef_taban_dalı_veya_commit_değeri</span>

- Bir birleştirme hatası tarafından durdurulan tekrar temelleme işlemini çekişen dosyaları düzenledikten sonra devam ettir:

`git rebase --continue`

- Birleştirme çatışmasından ötürü durdurulan tekrar temelleme işlemini çekişen commit'leri atlayarak devam ettir:

`git rebase --skip`

- Devam eden tekrar temelleme işlemini iptal et (örneğin birleştirmede çatışma yaşandığında):

`git rebase --abort`

- Mevcut dalın bir parçasını belirtilen eski tabandan yeni tabana taşı:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yeni_taban</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eski_taban</span>

- Son 3 commit'i etkileşimli olmayacak şekilde yeniden uygula:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Herhangi bir çatışmayı çalışan dal sürümünü kurtarmak üzere otomatik olarak çöz (`theirs` argümanı burada ters anlama sahip):

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>
