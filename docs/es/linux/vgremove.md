---
layout: page
title: linux/vgremove (español)
description: "Elimina grupo(s) de volúmenes en LVM."
content_hash: 6385fb446b306c0cb26be55879ca669d013566b9
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/vgremove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vgremove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vgremove

Elimina grupo(s) de volúmenes en LVM.
Más información: <https://manned.org/vgremove>.

- Elimina un grupo de volúmenes con confirmación:

`vgremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_volumen</span>

- Fuerza la eliminación de un grupo de volúmenes sin confirmación:

`vgremove --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_volumen</span>

- Establece el nivel de depuración para el registro detallado en el nivel 2, (repite `--debug` hasta 6 veces para aumentar el nivel):

`vgremove --debug --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_volumen</span>

- Utiliza una configuración específica para anular los valores predeterminados:

`vgremove --config '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">global/locking_type=1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_volumen</span>

- Muestra texto de ayuda para obtener información de uso:

`vgremove --help`
