---
layout: page
title: linux/aa-disable (español)
description: "Deshabilita las políticas de seguridad de AppArmor."
content_hash: ee402c1d17c7332dd4ab24974cbcc39659cf45d6
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/aa-disable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-disable

Deshabilita las políticas de seguridad de AppArmor.
Vea también: `aa-complain`, `aa-enforce`, `aa-status`.
Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Deshabilita perfil:

`sudo aa-disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/perfil1 ruta/a/perfil2 ...</span>

- Deshabilita perfiles (predeterminado a `/etc/apparmor.d`):

`sudo aa-disable --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/perfiles</span>
