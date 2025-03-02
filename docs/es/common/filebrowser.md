---
layout: page
title: common/filebrowser (español)
description: "Sencillo servidor web HTTP para gestionar archivos y directorios."
content_hash: 97c0fb0ae7f26a13218c27e7afd38d9686d0b923
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/filebrowser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# filebrowser

Sencillo servidor web HTTP para gestionar archivos y directorios.
Más información: <https://filebrowser.org>.

- Inicia una nueva instancia del servidor sirviendo el directorio actual:

`filebrowser`

- Inicia una nueva instancia de servidor sirviendo un directorio raíz específico:

`filebrowser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Inicia una instancia con una dirección de host (por defecto `127.0.0.1`) y un puerto (por defecto `8080`) diferentes:

`filebrowser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Inicia una instancia con un archivo de configuración especificado, almacenando la base de datos de la aplicación en una ubicación específica (por defecto es `filebrowser.db` en el directorio actual):

`filebrowser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--database</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/base_de_datos.db</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Configura un nombre de usuario y una contraseña diferentes para la primera cuenta (ambos por defecto `admin`) cuando configure una nueva instancia:

`filebrowser --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Configura la cantidad máxima de procesadores de imágenes utilizados al generar miniaturas (por defecto es `4`):

`filebrowser --img-processors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Desactiva las miniaturas de imágenes, así como la función Command Runner, que limita el acceso a los archivos de script alojados para que no se ejecuten dentro de la aplicación:

`filebrowser --disable-exec --disable-thumbnails `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Deshabilita el cambio de tamaño de las vistas previas de imágenes, así como la detección de tipos de archivo mediante la lectura de sus cabeceras:

`filebrowser --disable-preview-resize --disable-type-detection-by-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
