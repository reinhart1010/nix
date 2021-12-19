---
layout: page
title: linux/modinfo (italiano)
description: "Estrae le informazioni riguardarti un modulo del kernel Linux."
content_hash: 009ac24b50c64753f6008b70edda3c9c440ab4b3
related_topics:
  - title: English version
    url: /en/linux/modinfo.html
    icon: bi bi-globe
---
# modinfo

Estrae le informazioni riguardarti un modulo del kernel Linux.
Maggiori informazioni: <https://manned.org/modinfo>.

- Elenca tutti gli attributi di un modulo del kernel:

`modinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo_del_kernel</span>

- Elenca solamente gli attributi specificati:

`modinfo -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author|description|license|parm|filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo_del_kernel</span>
