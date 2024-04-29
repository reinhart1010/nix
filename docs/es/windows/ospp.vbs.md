---
layout: page
title: windows/ospp.vbs (español)
description: "Instala, activa y administra versiones con licencia por volumen de productos Microsoft Office."
content_hash: 07e573acfe6e2c9fdd94faa7998b15332d499094
last_modified_at: 2024-04-29
related_topics:
  - title: English version
    url: /en/windows/ospp.vbs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ospp.vbs

Instala, activa y administra versiones con licencia por volumen de productos Microsoft Office.
Nota: este comando puede anular, desactivar y/o eliminar tu volumen actual de versiones de productos Office con licencia, así que procede con cautela.
Más información: <https://learn.microsoft.com/deployoffice/vlactivation/tools-to-manage-volume-activation-of-office>.

- Instala una clave de producto (Nota: sustituye a la clave existente):

`cscript ospp.vbs /inpkey:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_producto</span>

- Desinstala una clave de producto instalada con los cinco últimos dígitos de la clave de producto:

`cscript ospp.vbs /unpkey:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_producto</span>

- Establece un nombre de host KMS:

`cscript ospp.vbs /sethst:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip|nombre_host</span>

- Establece un puerto KMS:

`cscript ospp.vbs /setprt:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Activa las claves de producto de Office instaladas:

`cscript ospp.vbs /act`

- Muestra la información de licencia de las claves de producto instaladas:

`cscript ospp.vbs /dstatus`
