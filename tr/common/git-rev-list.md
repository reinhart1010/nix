---
layout: page
title: common/git-rev-list (Türkçe)
description: "Değişiklikleri (commit'leri) ters kronolojik sırada sırala."
content_hash: 3a6349dbac6347effb75fb907aef50ca3f6fa649
related_topics:
  - title: English version
    url: /en/common/git-rev-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rev-list.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-list.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-list.html
    icon: bi bi-globe
---
# git rev-list

Değişiklikleri (commit'leri) ters kronolojik sırada sırala.
Daha fazla bilgi: <https://git-scm.com/docs/git-rev-list>.

- Mevcut daldaki tüm commit'leri sırala:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Belirtilen daldaki belirtilen tarihten daha yakın olan commit'leri sırala:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilen commit'deki tüm birleştirme commit'lerini sırala:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Belirtilen etiketten itibaren olan commit sayılarını çıkar:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>`..HEAD --count`
