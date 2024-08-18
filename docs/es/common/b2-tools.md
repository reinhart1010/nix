---
layout: page
title: common/b2-tools (español)
description: "Accede fácilmente a todas las funciones de Backblaze B2 Cloud Storage."
content_hash: b7befd91aa4b8812cc441b2e7db99d0f5e8d6e07
last_modified_at: 2024-08-18
related_topics:
  - title: English version
    url: /en/common/b2-tools.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/b2-tools.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># b2-tools

Accede fácilmente a todas las funciones de Backblaze B2 Cloud Storage.
Más información: <https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- Accede a tu cuenta:

`b2 authorize_account `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_id</span>

- Lista los buckets existentes en tu cuenta:

`b2 list_buckets`

- Crea un cubo, indica el nombre del cubo y el tipo de acceso (por ejemplo, allPublic o allPrivate):

`b2 create_bucket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_cubo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">allPublic|allPrivate</span>

- Sube un archivo. Elige un archivo, un bucket y una carpeta:

`b2 upload_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_cubo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_carpeta</span>

- Sube un directorio de origen a un destino de Backblaze B2 bucket:

`b2 sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_cubo</span>

- Copia un archivo de un bucket a otro bucket:

`b2 copy-file-by-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_origen</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_cubo_destino</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo/b2</span>

- Muestra los archivos de tu bucket:

`b2 ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_bucket</span>

- Elimina una "carpeta" o un conjunto de archivos que coincidan con un patrón:

`b2 rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/carpeta|patrón</span>
