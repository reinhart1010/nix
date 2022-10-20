---
layout: page
title: common/chgrp (italiano)
description: "Cambia il gruppo proprietario di file e directory."
content_hash: 35bc60539bb0da7b128c7ab6a46ad9c8a8074d58
related_topics:
  - title: English version
    url: /en/common/chgrp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chgrp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chgrp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chgrp.html
    icon: bi bi-globe
---
# chgrp

Cambia il gruppo proprietario di file e directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/chgrp>.

- Cambia il gruppo proprietario di un file/directory:

`chgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Cambia ricorsivamente il gruppo proprietario di una directory e dei suoi contenuti:

`chgrp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Cambia il gruppo proprietario di un link simbolico:

`chgrp -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/symlink</span>

- Cambia il gruppo proprietario di un file/directory rendendolo uguale a quello di un altro file di riferimento:

`chgrp --reference=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_riferimento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
