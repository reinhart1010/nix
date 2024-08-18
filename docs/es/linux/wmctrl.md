---
layout: page
title: linux/wmctrl (español)
description: "CLI para X Window Manager."
content_hash: 50474ea06a286d4d0e8736d0a28772a34d6798ab
last_modified_at: 2024-08-18
related_topics:
  - title: English version
    url: /en/linux/wmctrl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wmctrl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wmctrl

CLI para X Window Manager.
Más información: <https://manned.org/wmctrl>.

- Lista todas las ventanas, gestionadas por el gestor de ventanas:

`wmctrl -l`

- Cambia a la primera ventana cuyo título (parcial) coincida:

`wmctrl -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_ventana</span>

- Mueve una ventana al espacio de trabajo actual, levántala y dale foco:

`wmctrl -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_ventana</span>

- Cambia a un espacio de trabajo:

`wmctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_espacio_de_trabajo</span>

- Selecciona una ventana y activa la pantalla completa:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_ventana</span>` -b toggle,fullscreen`

- Selecciona una ventana y muévela a un espacio de trabajo:

`wmctrl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título_ventana</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_espacio_de_trabajo</span>
