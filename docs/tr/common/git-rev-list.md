---
layout: page
title: common/git-rev-list (Türkçe)
description: "Değişiklikleri (commit'leri) ters kronolojik sırada sırala."
content_hash: 58c26eac7c3cbc0b84d4ff20e27ec13eb4cf7240
last_modified_at: 2023-11-12
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git rev-list

Değişiklikleri (commit'leri) ters kronolojik sırada sırala.
Daha fazla bilgi için: <https://git-scm.com/docs/git-rev-list>.

- Mevcut daldaki tüm commit'leri sırala:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Belirtilen daldaki belirtilen tarihten daha yakın olan commit'leri sırala:

`git rev-list --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'2019-12-01 00:00:00'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_ismi</span>

- Belirtilen commit'deki tüm birleştirme commit'lerini sırala:

`git rev-list --merges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Belirtilen etiketten itibaren olan commit sayılarını çıkar:

`git rev-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_name</span>`..HEAD --count`
