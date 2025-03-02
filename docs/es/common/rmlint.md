---
layout: page
title: common/rmlint (español)
description: "Encuentra desperdicio de espacio y otras cosas rotas en tu sistema de archivos."
content_hash: 2b51a45fabe76199e6bf4622beda2c4091d4ac5e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/rmlint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rmlint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmlint

Encuentra desperdicio de espacio y otras cosas rotas en tu sistema de archivos.
Más información: <https://rmlint.readthedocs.io/en/latest/rmlint.1.html>.

- Comprueba los directorios en busca de archivos duplicados, vacíos y rotos:

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio1 ruta/a/directorio2 ...</span>

- Comprueba si hay duplicados mayores a un tamaño determinado, preferiblemente manteniendo los archivos en directorios etiquetados (después de la doble barra):

`rmlint -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1MB</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_original</span>

- Comprueba que no se desperdicia espacio, manteniendo todo en los directorios no etiquetados:

`rmlint --keep-all-untagged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_original</span>

- Elimina archivos duplicados encontrados tras una ejecución de `rmlint`:

`./rmlint.sh`

- Encuentra árboles de directorios duplicados basándose en los datos, ignorando los nombres:

`rmlint --merge-directories `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Marca archivos en la profundida[d] de la ruta inferior como originales, en caso de igualdad elegir uno más corto [l]:

`rmlint --rank-by=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Encuentra archivos con idéntico nombre de archivo y contenido, y vincula en lugar de eliminar los duplicados:

`rmlint -c sh:link --match-basename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- Utiliza `data` como directorio maestro. Busca solo los duplicados de la copia de seguridad que también estén en `datos`. No elimina ningún archivo de "datos":

`rmlint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/copia</span>` // `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/datos</span>` --keep-all-tagged --must-match-tagged`
