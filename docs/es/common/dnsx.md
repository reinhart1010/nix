---
layout: page
title: common/dnsx (español)
description: "Un equipo de herramientas de DNS rápido y multipropósito para ejecutar múltiples consultas DNS."
content_hash: 06fee9a47d817b2e3c40a6e185f05c500fa99dc3
last_modified_at: 2024-05-12
related_topics:
  - title: English version
    url: /en/common/dnsx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnsx

Un equipo de herramientas de DNS rápido y multipropósito para ejecutar múltiples consultas DNS.
Nota: la entrada a `dnsx` necesita ser pasada a través de `stdin` (tubería `|`) en algunos casos.
Ver también: `dig`, `dog`, `dnstracer`.
Más información: <https://github.com/projectdiscovery/dnsx>.

- Consulta el registro A de un subdominio y muestra la [re]spuesta recibida:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` | dnsx -a -re`

- Consulta todos los registros DNS (A, AAAA, CNAME, NS, TXT, SRV, PTR, MX, SOA, AXFR y CAA):

`dnsx -recon -re <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>

- Consulta un tipo específico de registro DNS:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` | dnsx -re -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|cname|ns|txt|srv|ptr|mx|soa|any|axfr|caa</span>

- Muestra s[o]lo la [r]espuesta (no muestra el dominio o subdominio consultado):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` | dnsx -ro`

- Muestra la respuesta sin procesar una consulta, especificando los solucionado[r]es a utilizar y el número de intentos en caso de haber errores:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` | dnsx -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|raw</span>` -resolver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1,8.8.8.8,...</span>` -retry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>

- Aplica fuerza bruta a registros DNS utilizando un marcador de posición:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FUZZ.ejemplo.com</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lista_de_palabras.txt</span>` -re`

- Aplica fuerza bruta a registros DNS a partir de una lista de [d]ominios y listas de palabras, adjuntando la salida a un archivo sin códigos de [c]olor:

`dnsx -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/dominio.txt</span>` -wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lista_de_palabras.txt</span>` -re -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida.txt</span>` -no-color`

- Extrae registros `CNAME` desde una lista de subdominios, con una velocidad [l]ímite de consultas DNS por segundo:

`subfinder -silent -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` | dnsx -cname -re -rl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>
