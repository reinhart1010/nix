---
layout: page
title: common/git-checkout (Türkçe)
description: "Bulunulan dalı değiştir veya çalışma ağaçlarını onar."
content_hash: f5cdaa7343baff72b3022329a00353abb67184d9
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
---
# git checkout

Bulunulan dalı değiştir veya çalışma ağaçlarını onar.
Daha fazla bilgi: <https://git-scm.com/docs/git-checkout>.

- Yeni bir dal oluştur ve bu dala geç:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilen bir referansa (dal, uzak/dal, etiket gibi) dayanacak şekilde yeni bir dal oluştur ve bu dala geç:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">referans</span>

- Varolan yerel bir dala geç:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- En son kontrol edilmiş olan dala geç:

`git checkout -`

- Uzak bağlantıdaki varolan bir dala geç:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uzak_bağlantı_adresi</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Mevcut dizindeki sahnelenmemiş tüm değişiklikleri ayır (geri alma benzeri bir komut için `git reset` komutu önerilir):

`git checkout .`

- Sahnelenmemiş değişiklikleri belirtilen dosyaya ayır:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_ismi</span>

- Mevcut dizindeki bir dosyayı, belirtilen dalda commit edilmiş sürümü ile değiştirin:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya_ismi</span>
