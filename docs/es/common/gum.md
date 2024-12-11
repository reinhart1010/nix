---
layout: page
title: common/gum (español)
description: "Produce guiones glamorosos para el intérprete de comando."
content_hash: dd7b2bbd3d3604d488b5b0b47bf48c3bf34911f0
last_modified_at: 2024-12-11
related_topics:
  - title: English version
    url: /en/common/gum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gum.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gum

Produce guiones glamorosos para el intérprete de comando.
Más información: <https://github.com/charmbracelet/gum>.

- Ofrece varias opciones para elegir una y la imprime en `stdout`:

`gum choose "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción_1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción_2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opción_3</span>`"`

- Muestra una entrada de texto interactiva para que el usuario introduzca una cadena con un texto indicativo (placeholder) específico:

`gum input --placeholder "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>`"`

- Abre un aviso de confirmación interactivo y sale con `0` o `1`:

`gum confirm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¿Continuar?</span>`" --default=false --affirmative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Sí</span>`" --negative "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">No</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">&& echo "Seleccionó Sí" || echo "Seleccionó No"</span>

- Muestra un spinner con un texto acompañante mientras se ejecuta una orden:

`gum spin --spinner `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cargando...</span>`" -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">orden</span>

- Formatea texto para incluir emojis:

`gum format -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emoji</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:smile: :heart: hola</span>`"`

- Solicita texto de varias líneas interactivamente (CTRL + D para salvar) y escribir en `datos.txt`:

`gum write > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datos.txt</span>
