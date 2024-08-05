---
layout: page
title: common/accelerate (español)
description: "Una biblioteca que permite ejecutar el mismo código PyTorch en cualquier configuración distribuida."
content_hash: 1dd7d97a7d6bee8d109f6527adba821f96260482
last_modified_at: 2024-08-05
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# accelerate

Una biblioteca que permite ejecutar el mismo código PyTorch en cualquier configuración distribuida.
Más información: <https://huggingface.co/docs/accelerate/index>.

- Imprime información del entorno:

`accelerate env`

- Crea interactivamente un archivo de configuración:

`accelerate config`

- Imprime el coste estimado en memoria de la GPU al ejecutar un modelo Hugging Face con distintos tipos de datos:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre/modelo</span>

- Prueba un archivo de configuración de Accelerate:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/config.yaml</span>

- Ejecuta un modelo en CPU con Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Ejecuta un modelo en multi-GPU con Accelerate, con 2 máquinas:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.py</span>` --multi_gpu --num_machines 2`
