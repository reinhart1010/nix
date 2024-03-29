---
layout: page
title: common/git-bisect (Türkçe)
description: "Bug taşıyan commit'i bulmak için ikili arama kullan."
content_hash: 80fdd9012c9cdc2c88c0de72b4eef8dc8b93b15e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bisect

Bug taşıyan commit'i bulmak için ikili arama kullan.
Git otomatik olarak commit çizelgesi içinde oradan oraya atlayarak yaramaz commit'i saptar.
Daha fazla bilgi için: <https://git-scm.com/docs/git-bisect>.

- Buglı bilinen bir commit'i ve (genelde eski olan) iyi bir commit'i belirterek ikiye bölme işlemini başlat:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kötü_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iyi_commit</span>

- `git bisect`'in seçtiği her commit'i, mevcut soruna sebep olup olmadıklarını test ettikten sonra "bad" (kötü) veya "good" (iyi) olarak işaretle:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- `git bisect` sorunlu commit'i saptadıktan sonra, ikiye bölme işlemini bitir ve depoyu bahsi geçen commit'den önceki dala geçir:

`git bisect reset`

- İkiye bölme işlemi sırasında bir commit'i atla:

`git bisect skip`
