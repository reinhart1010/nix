---
layout: page
title: osx/automount (español)
description: "Lee el archivo `/etc/auto_master` y monta `autofs` en los puntos de montaje apropiados para activar el montaje bajo demanda de directorios. Esencialmente, es una forma de iniciar manualmente el proceso de automontaje del sistema."
content_hash: 604ada5676d3981affb97aa8d1d4217c0b9dd8d6
last_modified_at: 2024-08-08
related_topics:
  - title: English version
    url: /en/osx/automount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/automount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># automount

Lee el archivo `/etc/auto_master` y monta `autofs` en los puntos de montaje apropiados para activar el montaje bajo demanda de directorios. Esencialmente, es una forma de iniciar manualmente el proceso de automontaje del sistema.
Nota: Lo más probable es que necesites ejecutarlo con `sudo` si no tienes los permisos necesarios.
Más información: <https://keith.github.io/xcode-man-pages/automount.8.html>.

- Ejecuta automount, vacía la caché(`-c`) de antemano, y es detallista(`-v`) al respecto (uso más común):

`automount -cv`

- Desmonta automáticamente transcurridos 5 minutos (300 segundos) de inactividad:

`automount -t 300`

- Desmonta cualquier cosa previamente montada por automount y/o definida en `/etc/auto_master`:

`automount -u`
