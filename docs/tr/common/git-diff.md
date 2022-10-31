---
layout: page
title: common/git-diff (Türkçe)
description: "İzlenen dosyalara değişiklikleri göster."
content_hash: 2f6f04d1f0e021dda49c64335d13ada85acf3edf
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
---
# git diff

İzlenen dosyalara değişiklikleri göster.
Daha fazla bilgi için: <https://git-scm.com/docs/git-diff>.

- Sahnelenmemiş, commit'lenmemiş değişiklikleri göster:

`git diff`

- Sahnelenmiş olanlar da dahil olmak üzere tüm commit'lenmemiş değişiklikleri göster:

`git diff HEAD`

- Yalnızca sahnelenmiş (eklenmiş ancak commit'lenmemiş) değişiklikleri göster:

`git diff --staged`

- Belirtilen bir tarihten itibaren yapılmış tüm commit'lerdeki değişiklikleri göster:

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Belirtilen bir commit'ten itibaren yalnızca üzerinde değişiklik yapılmış dosyaların ismini göster:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Belirtilen bir commit'ten itibaren yapılmış dosya oluşturma, yeniden adlandırma ve mod değişim işlemlerini göster:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Tek bir dosyayı iki dal veya commit arasında karşılaştır:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>

- Mevcut daldaki farklı dosyaları başka bir daldakilerle karşılaştır:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">örnek/dosya</span>
