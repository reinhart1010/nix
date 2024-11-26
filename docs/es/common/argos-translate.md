---
layout: page
title: common/argos-translate (español)
description: "Una biblioteca de traducción local (offline) de código abierto y una herramienta CLI escrita en Python."
content_hash: 9bf2c78cad2aaec2b5f52872b6d4bb4263573694
last_modified_at: 2024-11-26
related_topics:
  - title: English version
    url: /en/common/argos-translate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/argos-translate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># argos-translate

Una biblioteca de traducción local (offline) de código abierto y una herramienta CLI escrita en Python.
Más información: <https://www.argosopentech.com/>.

- Instala pares de traducción del español al inglés:

`argospm install translate-es_en`

- Traduce un texto del español (`es`) al inglés (`en`) (Nota: sólo se admiten códigos de dos letras para los idiomas:

`argos-translate --from-lang es --to-lang en `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">un texto corto</span>

- Traduce un archivo de texto del inglés al hindi:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.txt</span>` | argos-translate --from-lang en --to-lang hi`

- Lista todos los pares de traducción instalados:

`argospm list`

- Muestra pares de traducción del inglés que están disponibles para ser instalados:

`argospm search --from-lang en`

- Actualiza pares de paquetes de lenguaje instalados:

`argospm update`

- Traduce de `ar` a `ru` (Nota: esto requiere que se instalen los pares de traducción `translate-ar_en` y `translate-en_ru`):

`argos-translate --from-lang ar --to-lang ru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">صورة تساوي أكثر من ألف كلمة</span>
