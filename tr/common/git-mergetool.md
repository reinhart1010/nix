---
layout: page
title: common/git-mergetool (Türkçe)
description: "Birleştirme sırasında yaşanan karışıklıkları çözmek için karışıklık çözücü araçları çalıştırır."
content_hash: d36f3373e89ade6ea3be80f1067f30b0918e457a
related_topics:
  - title: English version
    url: /en/common/git-mergetool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mergetool.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git mergetool

Birleştirme sırasında yaşanan karışıklıkları çözmek için karışıklık çözücü araçları çalıştırır.
Daha fazla bilgi için: <https://git-scm.com/docs/git-mergetool>.

- Karışıklıkları çözmek için varsayılan birleştirme aracını başlat:

`git mergetool`

- Kullanılabilir birleştirme araçlarını sırala:

`git mergetool --tool-help`

- Belirtilen birleştirme aracını başlat:

`git mergetool --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">araç_ismi</span>

- Her birleştirme aracı çağrılışında harekete geçme:

`git mergetool --no-prompt`

- Özellikle grafiksel (GUI) birleştirme aracını kullan (merge.guitool değişkenine göz at):

`git mergetool --gui`

- Özellikle normal birleştirme aracını kullan (merge.guitool değişkenine göz at):

`git mergetool --no-gui`
