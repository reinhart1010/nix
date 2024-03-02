---
layout: page
title: linux/grubby (español)
description: "Herramienta para configurar los gestores de arranque `grub` y `zipl`."
content_hash: dae1f33fbc05a3f683340b90db44515ec427d301
last_modified_at: 2024-03-02
related_topics:
  - title: English version
    url: /en/linux/grubby.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grubby.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grubby

Herramienta para configurar los gestores de arranque `grub` y `zipl`.
Más información: <https://manned.org/man/grubby.8>.

- Añade argumentos de arranque del núcleo a todas las entradas del menú del núcleo:

`sudo grubby --update-kernel=ALL --args '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet console=ttyS0</span>`'`

- Elimina los argumentos existentes de la entrada para el núcleo por defecto:

`sudo grubby --update-kernel=DEFAULT --remove-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quiet</span>

- Lista todas las entradas del menú del núcleo:

`sudo grubby --info=ALL`
