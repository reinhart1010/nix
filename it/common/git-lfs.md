---
layout: page
title: common/git-lfs (italiano)
description: "Lavora con file di grandi dimensioni in repository Git."
content_hash: ecd2e1d50397ebbb5085adddbf78e0c797c83eba
related_topics:
  - title: English version
    url: /en/common/git-lfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-lfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-lfs.html
    icon: bi bi-globe
---
# git lfs

Lavora con file di grandi dimensioni in repository Git.
Maggiori informazioni: <https://git-lfs.github.com>.

- Inizializza Git LFS:

`git lfs install`

- Tieni traccia dei file che soddisfano un criterio glob:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Cambia l'URL endpoint di Git LFS (utile quando server LFS e server Git sono separati):

`git config -f .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfs_url_endpoint</span>

- Elenca i criteri tracciati:

`git lfs track`

- Elenca i file tracciati che sono già stati salvati in un commit:

`git lfs ls-files`

- Invia tutti gli oggetti Git LFS al server remoto (utile in caso di errori):

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_repository_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Scarica tutti gli oggetti Git LFS:

`git lfs fetch`

- Ripristina gli oggetti Git LFS:

`git lfs checkout`
