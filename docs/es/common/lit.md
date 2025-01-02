---
layout: page
title: common/lit (español)
description: "Comprobador integrado LLVM para ejecutar conjuntos de pruebas estilo LLVM y Clang, resumiendo los resultados."
content_hash: 48c1d0a3f8d85e872a86c1e541af2f00edd0ec74
last_modified_at: 2025-01-02
related_topics:
  - title: English version
    url: /en/common/lit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lit

Comprobador integrado LLVM para ejecutar conjuntos de pruebas estilo LLVM y Clang, resumiendo los resultados.
Parte de LLVM.
Más información: <https://www.llvm.org/docs/CommandGuide/lit.html>.

- Ejecuta un caso de prueba especificado:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_prueba.test</span>

- Ejecuta todos los casos de prueba en un directorio especificado:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/suite_de_pruebas</span>

- Ejecuta todos los escenarios de prueba y comprueba el tiempo de ejecución de cada uno de ellos:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/suite_de_pruebas</span>` --time-tests`

- Ejecuta pruebas individuales con Valgrind (comprobación de memoria y prueba de fuga de memoria):

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_prueba.test</span>` --vg --vg-leak --vg-args=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args_con_valgrind</span>
