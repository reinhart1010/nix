---
layout: page
title: common/git-flow (Türkçe)
description: "Üst seviye depo işlemleri için Git uzantı koleksiyonu."
content_hash: e04c1d9885f2ec28ef2c3e75322ddc1e402c872a
related_topics:
  - title: English version
    url: /en/common/git-flow.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-flow.html
    icon: bi bi-globe
---
# git flow

Üst seviye depo işlemleri için Git uzantı koleksiyonu.
Daha fazla bilgi için: <https://github.com/nvie/gitflow>.

- Varolan bir git deposu içinde başlat:

`git flow init`

- `develop` tabanlı bir özellik dalı üzerinde geliştirmeye başla:

`git flow feature start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">özellik</span>

- Özellik dalı üzerinde geliştirmeyi bitir, `develop` dalı ile birleştir ve dalı sil:

`git flow feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">özellik</span>

- Özelliği uzak sunucuya yayınla:

`git flow feature publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">özellik</span>

- Başka bir kullanıcı tarafından yayınlanan özelliği al:

`git flow feature pull origin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">özellik</span>
