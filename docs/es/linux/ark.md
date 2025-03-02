---
layout: page
title: linux/ark (español)
description: "Herramienta de archivado de KDE."
content_hash: 8e20b99462879a80671c88b2ce9f2124ec2241f4
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/ark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/ark.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/ark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ark

Herramienta de archivado de KDE.
Más información: <https://docs.kde.org/stable5/en/ark/ark/>.

- Extrae un archivo específico en el directorio actual:

`ark --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Extrae un archivo en un directorio específico:

`ark --batch --destination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Crea un archivo si no existe y agrega archivos específicos al mismo:

`ark --add-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>
