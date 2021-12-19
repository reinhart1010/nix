---
layout: page
title: common/git-restore (italiano)
description: "Ripristina i file dell'albero di lavoro. Richiede versioni di Git successive alla 2.23."
content_hash: e2e13edd9f7b0fbfbfe1c19848cfc2d0e16964c3
related_topics:
  - title: English version
    url: /en/common/git-restore.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-restore.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-restore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git restore

Ripristina i file dell'albero di lavoro. Richiede versioni di Git successive alla 2.23.
Vedi anche `git checkout`.
Maggiori informazioni: <https://git-scm.com/docs/git-restore>.

- Ripristina un file cancellato dal contenuto del commit corrente (HEAD):

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Ripristina un file alla versione di un commit differente:

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Annulla le modifiche ai file nell'area di stage, ripristinandoli all'HEAD:

`git restore .`
