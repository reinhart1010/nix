---
layout: page
title: common/clj (português (Brasil))
description: "Ferramenta de Clojure para iniciar um REPL ou invocar uma função com argumentos."
content_hash: e521aacd0fdf37dafa192fed76e31b0a3ae0179b
related_topics:
  - title: English version
    url: /en/common/clj.html
    icon: bi bi-globe
---
# clj

Ferramenta de Clojure para iniciar um REPL ou invocar uma função com argumentos.
Todas as opções podem ser definidas em um arquivo `deps.edn`.
Mais informações: <https://clojure.org/guides/deps_and_cli>.

- Inicia um REPL:

`clj`

- Executa uma função:

`clj -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace/function_name</span>

- Executa a função principal (*main*) do *namespace* especificado:

`clj -M -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

- Prepara um projeto resolvendo dependências, baixando bibliotecas, e criando / cacheando *classpaths*:

`clj -P`

- Inicia um servidor nREPL com o *middleware* CIDER:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"</span>`}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Inicia um REPL para ClojureScript e abre um navegador web:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"</span>`}' --main cljs.main --repl`
