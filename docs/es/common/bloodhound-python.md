---
layout: page
title: common/bloodhound-python (español)
description: "Un ingestor Python para BloodHound, utilizado para enumerar las relaciones de Active Directory."
content_hash: 3e2b495a8b23ad7fae8af43cab9a368fb9c9af3a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/bloodhound-python.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bloodhound-python

Un ingestor Python para BloodHound, utilizado para enumerar las relaciones de Active Directory.
Más información: <https://github.com/dirkjanm/BloodHound.py>.

- Recopila todos los datos utilizando los métodos de recopilación predeterminados (incluye grupos, sesiones y fideicomisos):

`bloodhound-python --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>

- Recopila datos utilizando la autenticación Kerberos sin requerir una contraseña en texto plano:

`bloodhound-python --collectionmethod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Todos</span>` --kerberos --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>

- Se autentica utilizando hashes NTLM en lugar de una contraseña:

`bloodhound-python --collectionmethod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Todos</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --hashes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LM:NTLM</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>

- Especifica un servidor de nombres personalizado para consultas DNS:

`bloodhound-python --collectionmethod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Todos}</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>` --nameserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_servidor</span>

- Guarde los archivos de salida como un archivo ZIP comprimido:

`bloodhound-python --collectionmethod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Todos</span>` --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dominio</span>` --zip`
