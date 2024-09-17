---
layout: page
title: common/chatgpt (español)
description: "Shell script para usar ChatGPT de OpenAI y DALL-E desde la terminal."
content_hash: 0c326b1ac1058f640a40e79abb05d96215103033
last_modified_at: 2024-09-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chatgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chatgpt

Shell script para usar ChatGPT de OpenAI y DALL-E desde la terminal.
Más información: <https://github.com/0xacx/chatGPT-shell-cli>.

- Comienza en modo chat:

`chatgpt`

- Da un [p]rompt para responder:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¿Cuál es la expresión regular para emparejar una dirección de correo electrónico?</span>`"`

- Inicia en modo chat utilizando un [m]odelo específico (por defecto es `gpt-3.5-turbo`):

`chatgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-4</span>

- Inicia en modo chat con un prompt [i]nicial:

`chatgpt --init-prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Tú eres Rick, de Rick y Morty. Responde a las preguntas usando su amaneramiento e incluye chistes insultantes.</span>`"`

- Envía el resultado de un comando a ChatGPT como un prompt:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¿Cómo ver los procesos en ejecución en Ubuntu?</span>`" | chatgpt`

- Genera una imagen utilizando DALL-E:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image: Un gato blanco</span>`"`
