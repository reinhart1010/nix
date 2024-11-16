---
layout: page
title: common/keybase (español)
description: "Directorio de claves que conecta identidades en redes sociales a claves encriptadas de una manera públicamente auditable."
content_hash: 4a5fe3a0370944dbaa23cc9b6b3b827bf1eb160f
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/keybase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/keybase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# keybase

Directorio de claves que conecta identidades en redes sociales a claves encriptadas de una manera públicamente auditable.
Más información: <https://keybase.io/docs/command_line>.

- Sigue a otro usuario:

`keybase follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Añade una nueva prueba:

`keybase prove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario_en_el_servicio</span>

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
