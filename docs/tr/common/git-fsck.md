---
layout: page
title: common/git-fsck (Türkçe)
description: "Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula."
content_hash: db869d57f1bf52102c1c04fdf5f60c4cf3a1af01
related_topics:
  - title: English version
    url: /en/common/git-fsck.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
---
# git fsck

Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula.
Düzenleme yapılması tavsiye edilmez. Geçersiz düğümleri çözmek için `git gc` komutu önerilir.
Daha fazla bilgi: <https://git-scm.com/docs/git-fsck>.

- Mevcut depoyu kontrol et:

`git fsck`

- Bulunan tüm etiketleri sırala:

`git fsck --tags`

- Bulunan tüm kök düğümleri sırala:

`git fsck --root`
