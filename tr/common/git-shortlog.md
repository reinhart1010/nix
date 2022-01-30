---
layout: page
title: common/git-shortlog (Türkçe)
description: "'git log' çıktısını özetle."
content_hash: 5ffcc31f60cea00e21021e81848a1be7ffaf5a1e
related_topics:
  - title: English version
    url: /en/common/git-shortlog.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-shortlog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-shortlog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-shortlog.html
    icon: bi bi-globe
---
# git shortlog

'git log' çıktısını özetle.
Daha fazla bilgi: <https://git-scm.com/docs/git-shortlog>.

- Yapılan tüm commit'lerin yazar ismiyle alfabetik olarak guruplanmış özetini göster:

`git shortlog`

- Yapılan tüm commit'lerin en çok commit yapan yazar ismi en üstte olacak şekilde özetini göster:

`git shortlog -n`

- Yapılan tüm commit'lerin yazar bilgilerini (isim ve e-posta) gösterecek şekilde özetini göster:

`git shortlog -c`

- En son yapılan 5 commit'in özetini göster (sürüm aralığı belirt):

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- Mevcut daldaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog -sne`

- Tüm dallardaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog -sne --all`
