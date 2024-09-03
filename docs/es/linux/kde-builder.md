---
layout: page
title: linux/kde-builder (español)
description: "Construye fácilmente componentes de KDE desde tus repositorios fuente."
content_hash: cf7a98b231638e21113b9ad46dbb087429a95289
last_modified_at: 2024-09-03
related_topics:
  - title: English version
    url: /en/linux/kde-builder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kde-builder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kde-builder

Construye fácilmente componentes de KDE desde tus repositorios fuente.
Sustituye a `kdesrc-build`.
Más información: <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>.

- Inicializa `kde-builder`:

`kde-builder --initial-setup`

- Compila un componente KDE y sus dependencias desde el código fuente:

`kde-builder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_componente</span>

- Compila un componente sin actualizar el código local y sin compilar sus dependencias:

`kde-builder --no-src --no-include-dependencies `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_componente</span>

- Actualiza los directorios de compilación antes de compilar:

`kde-builder --refresh-build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_componente</span>

- Reanuda la compilación a partir de una dependencia determinada:

`kde-builder --resume-from=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">componente_de_dependencia</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_componente</span>

- Ejecuta un componente con un nombre de ejecutable determinado:

`kde-builder --run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_ejecutable</span>

- Construye todos los componentes configurados:

`kde-builder`

- Utiliza las bibliotecas del sistema en lugar de un componente si no se puede compilar:

`kde-builder --no-stop-on-failure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_componente</span>
