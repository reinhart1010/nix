---
layout: page
title: osx/say (español)
description: "Convierte texto a voz."
content_hash: 0fb9173a58437fc3c86b276a4e37a78286bdb776
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# say

Convierte texto a voz.
Más información: <https://keith.github.io/xcode-man-pages/say.1.html>.

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
