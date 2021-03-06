---
layout: page
title: common/git-stash (Türkçe)
description: "Yerel Git düzenlemelerini geçici bir alanda sakla."
content_hash: fa0032bd10ffb013cce0f312ecf965cb92183e5a
related_topics:
  - title: English version
    url: /en/common/git-stash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-stash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stash.html
    icon: bi bi-globe
---
# git stash

Yerel Git düzenlemelerini geçici bir alanda sakla.
Daha fazla bilgi: <https://git-scm.com/docs/git-stash>.

- Yeni (izlenmeyen) dosyalar hariç mevcut değişiklikleri sakla:

`git stash [push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyfi_saklama_mesajı</span>`]`

- Yeni (izlenmeyen) dosyalar dahil mevcut değişiklikleri sakla:

`git stash -u`

- Değiştirilen dosyaların parçalarını etkileşimli şekilde seçip sakla:

`git stash -p`

- Tüm saklananları göster (saklanan ismi, bağlı olduğu dal ve mesaj gösterilir):

`git stash list`

- Bir saklananı uygula (varsayılan son saklanandır ve stash@{0} olarak belirtilir):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyfi_saklanan_veya_commit_ismi</span>

- Bir saklananı uygula (varsayılan stash@{0}), ve eğer uygulanması sıkıntı çıkarmıyorsa onu saklanan listesinden kaldır:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyfi_saklanan_ismi</span>

- Bir saklananı bırak (varsayılan stash@{0}):

`git stash drop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keyfi_saklanan_ismi</span>

- Tüm saklananları bırak:

`git stash clear`
