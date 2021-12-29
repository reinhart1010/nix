---
layout: page
title: common/git-difftool (Türkçe)
description: "Harici diff araçları kullanarak dosya değişimlerini göster. `git diff` ile aynı ayar ve argümanları destekler."
content_hash: a6ee37909d9ce97b18acdb6a16cccaee839a91a6
related_topics:
  - title: English version
    url: /en/common/git-difftool.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-difftool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-difftool.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git difftool

Harici diff araçları kullanarak dosya değişimlerini göster. `git diff` ile aynı ayar ve argümanları destekler.
Daha fazla bilgi için: <https://git-scm.com/docs/git-difftool>.

- Müsait diff araçlarını göster:

`git difftool --tool-help`

- Varsayılan diff aracını birleştirmeye ayarla:

`git config --global diff.tool "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meld</span>`"`

- Varsayılan diff aracını sahnelenmiş değişiklikleri göstermek için kullan:

`git difftool --staged`

- Verilen commit'den itibaren yapılmış değişiklikleri göstermek için (opendiff) kullan:

`git difftool --tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opendiff</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
