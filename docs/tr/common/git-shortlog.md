---
layout: page
title: common/git-shortlog (Türkçe)
description: "'git log' çıktısını özetle."
content_hash: 9073fc119c8ae202a6a4e0255c5013c56083985f
last_modified_at: 2024-10-13
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
  - title: 한국어 version
    url: /ko/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

'git log' çıktısını özetle.
Daha fazla bilgi için: <https://git-scm.com/docs/git-shortlog>.

- Yapılan tüm commit'lerin yazar ismiyle alfabetik olarak guruplanmış özetini göster:

`git shortlog`

- Yapılan tüm commit'lerin en çok commit yapan yazar ismi en üstte olacak şekilde özetini göster:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>

- Yapılan tüm commit'lerin yazar bilgilerini (isim ve e-posta) gösterecek şekilde özetini göster:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--committer</span>

- En son yapılan 5 commit'in özetini göster (sürüm aralığı belirt):

`git shortlog HEAD~5..HEAD`

- Mevcut daldaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>

- Tüm dallardaki tüm kullanıcıları, e-postalarını ve yaptıkları commit sayısını göster:

`git shortlog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--summary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--numbered</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--email</span>` --all`
