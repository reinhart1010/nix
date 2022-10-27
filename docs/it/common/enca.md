---
layout: page
title: common/enca (italiano)
description: "Rileva e converti l'encoding di file di testo."
content_hash: 2d59368de50ce47cd55dc4ce45d6a9efdeb57eb8
related_topics:
  - title: English version
    url: /en/common/enca.html
    icon: bi bi-globe
---
# enca

Rileva e converti l'encoding di file di testo.
Maggiori informazioni: <https://github.com/nijel/enca>.

- Rileva l'encoding di uno o più file in base alla locale di sistema:

`enca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Rileva l'encoding specificando un linguaggio nel formato di locale POSIX/C (e.g. zh_CN, en_US):

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Converti file ad uno specifico encoding:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 ...</span>

- Crea una copia di un file esistente utilizzando un encoding diverso:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linguaggio</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding_finale</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_originale</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuovo_file</span>
