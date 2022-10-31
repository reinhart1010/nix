---
layout: page
title: common/git-restore (Türkçe)
description: "Çalışan ağaç dosyalarını onar. Git sürümü 2.23+ olmalıdır."
content_hash: 582b40da2935b2c55c679b18928e5ef6fc096b69
related_topics:
  - title: English version
    url: /en/common/git-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-restore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-restore.html
    icon: bi bi-globe
---
# git restore

Çalışan ağaç dosyalarını onar. Git sürümü 2.23+ olmalıdır.
`git checkout` ve `git reset` komutlarına da ayrıca bakılması tavsiye edilir.
Daha fazla bilgi için: <https://git-scm.com/docs/git-restore>.

- Sahnelenmemiş bir dosyayı mevcut commit'in sürümüne kavuştur:

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>

- Sahnelenmemiş bir dosyayı belirtilen commit'in sürümüne kavuştur:

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>

- İzlenen dosyalardaki sahnelenmemiş tüm değişiklikleri iptal et:

`git restore :/`

- Bir dosyayı sahnelenmemiş hale getir:

`git restore --staged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>

- Tüm dosyaları sahnelenmemiş hale getir:

`git restore --staged :/`

- Dosyalara yapılan sahnelenmiş veya sahnelenmemiş tüm değişiklikleri iptal et:

`git restore --worktree --staged :/`

- Onarılacak dosya parçalarını etkileşimli olarak seç:

`git restore --patch`
