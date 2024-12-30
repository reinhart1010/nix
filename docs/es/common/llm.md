---
layout: page
title: common/llm (español)
description: "Interactúa con modelos grandes de lenguaje (LLMs) a través de APIs y modelos remotos que pueden instalarse y ejecutarse en su máquina."
content_hash: 107e6b17c7769c6237cc01847b58e3edc8b94b13
last_modified_at: 2024-12-30
related_topics:
  - title: English version
    url: /en/common/llm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# llm

Interactúa con modelos grandes de lenguaje (LLMs) a través de APIs y modelos remotos que pueden instalarse y ejecutarse en su máquina.
Más información: <https://llm.datasette.io/en/stable/help.html>.

- Configura una clave API de OpenAI:

`llm keys set openai`

- Ejecuta un prompt:

`llm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Diez nombres divertidos para un pelícano</span>`"`

- Ejecuta un prompt de [s]istema contra un archivo:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>` | llm --system "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Explica este código</span>`"`

- Instala paquetes de PyPI en el mismo entorno que LLM:

`llm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete1 paquete2 ...</span>

- Descarga y ejecuta un prompt frente a un [m]odelo:

`llm --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">orca-mini-3b-gguf2-q4_0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">¿Cuál es la capital de Francia?</span>`"`

- Crea un prompt de [s]istema y lo [s]alva como una plantilla:

`llm --system '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Eres una torta de queso sensible</span>`' --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torta_de_queso_sensible</span>

- Establece un chat interactivo con un [m]odelo específico utilizando una plan[t]illa específica:

`llm chat --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chatgpt</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torta_de_queso_sensible</span>
