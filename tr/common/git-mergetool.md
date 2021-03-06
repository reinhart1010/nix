---
layout: page
title: common/git-mergetool (Türkçe)
description: "Birleştirme sırasında yaşanan karışıklıkları çözmek için karışıklık çözücü araçları çalıştırır."
content_hash: 8ef75cc78908a276f58a11ec4cc08ef7453d056e
related_topics:
  - title: English version
    url: /en/common/git-mergetool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mergetool.html
    icon: bi bi-globe
---
# git mergetool

Birleştirme sırasında yaşanan karışıklıkları çözmek için karışıklık çözücü araçları çalıştırır.
Daha fazla bilgi: <https://git-scm.com/docs/git-mergetool>.

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
