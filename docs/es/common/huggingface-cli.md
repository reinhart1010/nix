---
layout: page
title: common/huggingface-cli (español)
description: "Interactúa con Hugging Face Hub."
content_hash: 05ef00b78a33926e6f24198cf3068ea3b1f19fbf
last_modified_at: 2024-07-31
related_topics:
  - title: English version
    url: /en/common/huggingface-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# huggingface-cli

Interactúa con Hugging Face Hub.
Inicia sesión, gestiona la caché local, carga o descarga archivos.
Más información: <https://huggingface.co/docs/huggingface_hub/guides/cli>.

- Inicia sesión en Hugging Face Hub:

`huggingface-cli login`

- Muestra el nombre del usuario conectado:

`huggingface-cli whoami`

- Cierra sesión:

`huggingface-cli logout`

- Genera información sobre el entorno:

`huggingface-cli env`

- Descarga archivos de un repositorio e imprime la ruta (omite los nombres de archivo para descargar todo el repositorio):

`huggingface-cli download --repo-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_archivo1 nombre_archivo2 ...</span>

- Sube una carpeta entera o un archivo a Hugging Face:

`huggingface-cli upload --repo-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repo_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_repositorio_o_directorio_de_repositorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de repositorio_o_directorio</span>

- Escanea la caché para ver los repositorios descargados y su uso de disco:

`huggingface-cli scan-cache`

- Elimina la caché de forma interactiva:

`huggingface-cli delete-cache`
