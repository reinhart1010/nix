---
layout: page
title: linux/aa-complain (español)
description: "Establece una política de AppArmor en modo de queja."
content_hash: 9795f5a810c5d6c5a6728ea64017ac9b6fd0fe12
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/linux/aa-complain.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aa-complain.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-complain

Establece una política de AppArmor en modo de queja.
Vea también: `aa-disable`, `aa-enforce`, `aa-status`.
Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Establece la política en modo de queja:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/perfil1 ruta/a/perfil2 ...</span>

- Establece políticas en modo de queja:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/perfiles</span>
