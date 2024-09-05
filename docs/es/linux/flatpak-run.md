---
layout: page
title: linux/flatpak-run (español)
description: "Ejecuta aplicaciones y tiempos de ejecución flatpak."
content_hash: 2452b355a6c83982f9fdbcf70f1bb3b5890a1756
last_modified_at: 2024-09-05
related_topics:
  - title: English version
    url: /en/linux/flatpak-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flatpak run

Ejecuta aplicaciones y tiempos de ejecución flatpak.
Más información: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- Ejecuta una aplicación instalada:

`flatpak run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Ejecuta una aplicación instalada desde una rama específica, por ejemplo, stable, beta, master:

`flatpak run --branch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|beta|master|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>

- Ejecuta un shell interactivo dentro de un flatpak:

`flatpak run --command=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.example.app</span>
