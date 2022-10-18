---
layout: page
title: common/git-ls-tree (Türkçe)
description: "Bir ağaç nesnesinin içeriklerini sırala."
content_hash: 88f731bb8e49056bbaf11921677c767573009582
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
---
# git ls-tree

Bir ağaç nesnesinin içeriklerini sırala.
Daha fazla bilgi: <https://git-scm.com/docs/git-ls-tree>.

- Bir daldaki ağacın içeriklerini sırala:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dal_name</span>

- Bir commit üstündeki ağacın içeriklerini alt ağaçlara ayırarak sırala:

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>

- Bir commit üstündeki ağacın yalnızca dosya isimlerini göster:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_değeri</span>
