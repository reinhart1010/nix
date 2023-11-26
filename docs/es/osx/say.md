---
layout: page
title: osx/say (español)
description: "Convierte texto a voz."
content_hash: 6f00c5475b1867e87666d0b70b5c65a8c7cd22eb
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/osx/say.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/say.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/say.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># say

Convierte texto a voz.
Más información: <https://ss64.com/osx/say.html>.

- Di una frase en voz alta:

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Me gusta andar en mi bicicleta.</span>`"`

- Lee un archivo en voz alta:

`say --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_archivo.txt</span>

- Di una frase con una voz y un ritmo de voz personalizados:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voz</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabras_por_minuto</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Lo siento David, no puedo dejarte hacer eso.</span>`"`

- Lista las voces disponibles (cada voz habla en un idioma distinto):

`say --voice="?"`

- Di algo en polaco:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zosia</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Litwo, ojczyzno moja!</span>`"`

- Crea un archivo de audio con el texto hablado:

`say --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_fichero.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Aquí están los locos.</span>`"`
