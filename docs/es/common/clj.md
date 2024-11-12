---
layout: page
title: common/clj (español)
description: "Herramienta de Clojure para usar una interfaz interactiva (REPL) o invocar una función con datos."
content_hash: bc95e31aef6463a009ff80863c97762428fb8c3c
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/common/clj.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clj.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clj.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clj.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clj

Herramienta de Clojure para usar una interfaz interactiva (REPL) o invocar una función con datos.
Todas las opciones se pueden definir en un archivo `deps.edn`.
Más información: <https://clojure.org/guides/deps_and_cli>.

- Inicia una REPL (interfaz interactiva):

`clj`

- Ejecuta una función:

`clj -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace/nombre_de_función</span>

- Ejecuta la función principal de un espacio de nombres (namespace) especificado:

`clj -M -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Prepara un proyecto resolviendo dependencias, descargando bibliotecas y haciendo/cacheando rutas de clases (classpaths):

`clj -P`

- Inicia un servidor nREPL con el software intermedio (middleware) CIDER:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}</span>`' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Inicia un REPL de ClojureScript y abre un navegador web:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}</span>`' --main cljs.main --repl`
