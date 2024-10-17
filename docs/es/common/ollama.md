---
layout: page
title: common/ollama (español)
description: "Un ejecutor de modelos de lenguaje grande."
content_hash: 238f803e69a833ae1e1e17bce5e3bbeb3feae8af
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/ollama.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ollama

Un ejecutor de modelos de lenguaje grande.
Para ver una lista de los modelos disponibles, consulta <https://ollama.com/library>.
Más información: <https://github.com/ollama/ollama>.

- Inicia el demonio requerido para ejecutar otros comandos:

`ollama serve`

- Ejecuta un modelo y chatea con él:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modelo</span>

- Ejecuta un modelo con un solo mensaje:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modelo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje</span>

- Lista los modelos descargados:

`ollama list`

- Descarga/actualiza un modelo específico:

`ollama pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modelo</span>

- Lista los modelos en ejecución:

`ollama ps`

- Elimina un modelo:

`ollama rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modelo</span>

- Crea un modelo desde un `Modelfile` ([f]):

`ollama create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_nuevo_modelo</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/Modelfile</span>
