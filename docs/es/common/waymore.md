---
layout: page
title: common/waymore (español)
description: "Obtén las URLs de un dominio desde Wayback Machine, Common Crawl, Alien Vault OTX, URLScan y VirusTotal."
content_hash: 2e8f968847816caff8bbb3a9cbe1358205e0a5d0
last_modified_at: 2024-03-26
related_topics:
  - title: English version
    url: /en/common/waymore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# waymore

Obtén las URLs de un dominio desde Wayback Machine, Common Crawl, Alien Vault OTX, URLScan y VirusTotal.
Nota: A menos que se especifique lo contrario, los resultados se escriben en el directorio `results/` donde reside el archivo `config.yml` de waymore (por defecto en `~/.config/waymore/`).
Más información: <https://github.com/xnl-h4ck3r/waymore>.

- Busca URLs de un dominio (la salida suele estar en `~/.config/waymore/results/`):

`waymore -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Limita los resultados de la búsqueda para que solo incluyan una lista de URLs de un dominio y almacena los resultados en el archivo especificado:

`waymore -mode U -oU `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ejemplo.com-urls.txt</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Imprime solo los cuerpos de contenido de las URLs y almacena los resultados en el directorio especificado:

`waymore -mode R -oR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/ejemplo.com-url-responses</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Filtra los resultados especificando intervalos de fechas:

`waymore -from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDD|YYYMM|YYYY</span>` -to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AAAAMMDD|AAAAMMD|AAAAMMD</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>
