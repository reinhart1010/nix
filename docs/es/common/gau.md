---
layout: page
title: common/gau (español)
description: "Obtén todas las URLs: obtén las URLs conocidas de Open Threat Exchange de AlienVault, Wayback Machine y Common Crawl para cualquier dominio."
content_hash: e77d80010de5692c47160bd581151c2b8a9d5b9a
last_modified_at: 2024-03-25
related_topics:
  - title: English version
    url: /en/common/gau.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gau

Obtén todas las URLs: obtén las URLs conocidas de Open Threat Exchange de AlienVault, Wayback Machine y Common Crawl para cualquier dominio.
Más información: <https://github.com/lc/gau>.

- Obtén todas las URLs de un dominio de Open Threat Exchange de AlienVault, Wayback Machine, Common Crawl y URLScan:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Obtén URLs de varios dominios:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio1 dominio2 ...</span>

- Obtén todas las URLs de varios dominios en un archivo de entrada, ejecutando varios subprocesos:

`gau --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/dominios.txt}</span>

- Escribe los resultados en un archivo:

`gau `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` --o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/urls_encontradas.txt</span>

- Busca las URLs de un solo proveedor específico:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback|commoncrawl|otx|urlscan</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Busca las URLs de varios proveedores:

`gau --providers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wayback,otx,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Busca las URLs dentro de un intervalo de fechas específico:

`gau --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AAAAMM</span>` --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>
