---
layout: page
title: common/tgpt (español)
description: "Habla con un chatbot de IA sin necesidad de claves API."
content_hash: ca200e89f6680a3c91122c1023321381e6a6536b
last_modified_at: 2024-02-27
related_topics:
  - title: English version
    url: /en/common/tgpt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tgpt

Habla con un chatbot de IA sin necesidad de claves API.
Proveedores disponibles: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
Más información: <https://github.com/aandrew-me/tgpt>.

- Chatea con el proveedor por defecto (GPT-3.5-turbo):

`tgpt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Inicia el modo interactivo [m]ultilínea:

`tgpt --multiline`

- Genera [i]mágenes y las guarda en el directorio actual:

`tgpt --image "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Genera [c]ódigo con el proveedor por defecto (GPT-3.5-turbo):

`tgpt --code "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Chatea con un proveedor específico silenciosamente (sin animaciones):

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openai|opengpts|koboldai|phind|llama2|blackboxai</span>` --quiet --whole "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Genera y ejecuta comandos de intérprete utilizando un proveedor específico (con confirmación):

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">llama2</span>` --shell "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Pregunta con una clave de API, modelo, longitud máxima de respuesta, temperatura y `top_p` (necesario cuando se utiliza el proveedor `openai`):

`tgpt --provider openai --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key</span>`" --model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>`" --max-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --temperature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>` --top_p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Alimenta un archivo como pre-entrada adicional:

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blackboxai</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
