---
layout: page
title: common/keybase (español)
description: "Directorio de claves que conecta identidades en redes sociales a claves encriptadas de una manera públicamente auditable."
content_hash: 0a62b545ebafd4bc7cee76db73eccd3d4959067c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/keybase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# keybase

Directorio de claves que conecta identidades en redes sociales a claves encriptadas de una manera públicamente auditable.
Más información: <https://keybase.io/docs/command_line>.

- Sigue a otro usuario:

`keybase follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>

- Añade una nueva prueba:

`keybase prove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario_en_el_servicio</span>

- Firma un archivo:

`keybase sign --infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_entrada</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>

- Verifica un archivo firmado:

`keybase verify --infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_entrada</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>

- Encripta un archivo:

`keybase encrypt --infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_entrada</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receptor</span>

- Desencripta un archivo:

`keybase decrypt --infile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_entrada</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>

- Revoca el dispositivo actual, se desconecta y borra los datos locales:

`keybase deprovision`
