---
layout: page
title: common/git-ls-tree (Türkçe)
description: "Bir ağaç nesnesinin içeriklerini sırala."
content_hash: f99048f0d1b5cc847aa39117f007f75bfd08641b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-ls-tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-ls-tree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-tree.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git ls-tree

Bir ağaç nesnesinin içeriklerini sırala.
Daha fazla bilgi için: <https://git-scm.com/docs/git-ls-tree>.

- Bir daldaki ağacın içeriklerini sırala:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_name</span>

- Bir commit üstündeki ağacın içeriklerini alt ağaçlara ayırarak sırala:

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bir commit üstündeki ağacın yalnızca dosya isimlerini göster:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>
