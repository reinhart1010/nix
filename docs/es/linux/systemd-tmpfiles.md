---
layout: page
title: linux/systemd-tmpfiles (español)
description: "Crea, elimina y limpia archivos y directorios volátiles y temporales."
content_hash: ac46a37fa7e1d04392fd4f82ca64ff203f0d66a7
last_modified_at: 2024-04-06
related_topics:
  - title: English version
    url: /en/linux/systemd-tmpfiles.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-tmpfiles

Crea, elimina y limpia archivos y directorios volátiles y temporales.
Este comando es invocado automáticamente en el arranque por los servicios de systemd, ejecutarlo manualmente tiende a ser innecesario.
Más información: <https://www.freedesktop.org/software/systemd/man/systemd-tmpfiles.html>.

- Crea los archivos y directorios especificados en el archivo de configuración:

`systemd-tmpfiles --create`

- Limpia archivos y directorios con los parámetros de edad configurados:

`systemd-tmpfiles --clean`

- Elimina archivos y directorios según lo especificado en el archivo de configuración:

`systemd-tmpfiles --remove`

- Aplica operaciones en archivos de configuración específicos de usuario:

`systemd-tmpfiles --create --user`

- Ejecuta las líneas marcadas para el inicio del arranque:

`systemd-tmpfiles --create --boot`
