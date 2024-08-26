---
layout: page
title: common/aspell (español)
description: "Corrector ortográfico interactivo."
content_hash: f45fd4baa27ae8186b749dc2b3875f6c891f948c
last_modified_at: 2024-08-26
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aspell

Corrector ortográfico interactivo.
Más información: <http://aspell.net/>.

- Revisa la ortografía de un solo archivo:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Lista las palabras mal escritas de `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | aspell list`

- Muestra los idiomas disponibles en el diccionario:

`aspell dicts`

- Ejecuta `aspell` con un idioma diferente (toma el código de idioma ISO 639 de dos letras):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Lista las palabras mal escritas de `stdin` e ignora las palabras de la lista personal de palabras:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lista_personal_de_palabras.pws</span>` list`
