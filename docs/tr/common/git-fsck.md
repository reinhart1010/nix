---
layout: page
title: common/git-fsck (Türkçe)
description: "Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula:"
content_hash: 0ae2c974f1f98b51463c85a0dfe553abd50f5412
related_topics:
  - title: English version
    url: /en/common/git-fsck.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fsck.html
    icon: bi bi-globe
---
# git fsck

Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula:
Düzenleme yapılması tavsiye edilmez. Geçersiz düğümleri çözmek için `git gc` komutu önerilir.
Daha fazla bilgi: <https://git-scm.com/docs/git-fsck>.

- Mevcut depoyu kontrol et:

`git fsck`

- Bulunan tüm etiketleri sırala:

`git fsck --tags`

- Bulunan tüm kök düğümleri sırala:

`git fsck --root`
