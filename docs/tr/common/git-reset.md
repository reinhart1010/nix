---
layout: page
title: common/git-reset (Türkçe)
description: "Mevcut Git HEAD'ini belirtilen duruma sıfırlayarak commit'leri veya değişiklikleri geri al."
content_hash: 315c183b4100355e8c4e9e8adc1e027dca6e31b8
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/common/git-reset.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

Mevcut Git HEAD'ini belirtilen duruma sıfırlayarak commit'leri veya değişiklikleri geri al.
Eğer bir konum verildiye o konumdaki değişiklikler "geri alınır"; eğer bir commit değeri veya dal verildiyse o commit/dal "geri alınır".
Daha fazla bilgi için: <https://git-scm.com/docs/git-reset>.

- Her şeyi geri al:

`git reset`

- Belirtilen dosya(lar)ı geri al:

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya(ların)/konumu</span>

- Bir dosyanın kısımlarını geri al:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosya/konumu</span>

- Son commit'i, dosya sisteminde yapılan değişiklikleri geri almadan geri al:

`git reset HEAD~`

- Son iki commit'i onların indeks'e yaptığı değişiklikleri ekleyerek geri al:

`git reset --soft HEAD~2`

- Commit'lenmemiş değişiklikleri sahnelenip sahnelenmediklerine bakmaksızın iptal et (sadece sahnelenmemiş değişiklikleri iptal etmek için `git checkout` kullanılır):

`git reset --hard`

- Depoyu belirtilen commit'e o zamana kadar yapılan değişiklikleri iptal ederek sıfırla:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
