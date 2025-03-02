---
layout: page
title: linux/aa-enforce (español)
description: "Establece un perfil de AppArmor en modo de aplicación."
content_hash: 393b8d3d796699bf5e1f4891e10213682dede3da
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/aa-enforce.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/aa-enforce.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/aa-enforce.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aa-enforce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aa-enforce

Establece un perfil de AppArmor en modo de aplicación.
Vea también: `aa-complain`, `aa-disable`, `aa-status`.
Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Activa el perfil:

`sudo aa-enforce --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/perfil</span>

- Activa los perfiles:

`sudo aa-enforce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/perfil1 ruta/al/perfil2 ...</span>
