---
layout: page
title: common/dig (español)
description: "Utilidad de consulta para DNS."
content_hash: 4539349c8df52d70682884f6ec1f1336414926f9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dig

Utilidad de consulta para DNS.
Más información: <https://manned.org/dig>.

- Consulta la(s) IP(s) asociadas a un nombre de equipo (registros A):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Obtiene una respuesta detallada para un dominio determinado (registros A):

`dig +noall +answer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Consulta un tipo de registro DNS específico asociado a un dominio determinado:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>

- Obtiene todos los tipos de registros para un dominio determinado:

`dig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` ANY`

- Especifica un servidor DNS alterno a consultar:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Realiza una búsqueda DNS inversa para una dirección IP (registro PTR):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Encuentra servidores de nombre autoritativos para la zona y muestra registros SOA:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Realiza consultas iterativas y muestra el trazado de ruta completo para resolver un dominio:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
