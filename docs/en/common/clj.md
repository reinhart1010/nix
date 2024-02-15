---
layout: page
title: common/clj (English)
description: "Clojure tool to start a REPL or invoke a function with data."
content_hash: ab67b26823b69002825ae9d5e949071ac18f1c75
last_modified_at: 2024-02-15
related_topics:
  - title: Nederlands version
    url: /nl/common/clj.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clj.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clj

Clojure tool to start a REPL or invoke a function with data.
All options can be defined in a `deps.edn` file.
More information: <https://clojure.org/guides/deps_and_cli>.

- Start a REPL (interactive shell):

`clj`

- Execute a function:

`clj -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace/function_name</span>

- Run the main function of a specified namespace:

`clj -M -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

- Prepare a project by resolving dependencies, downloading libraries, and making/caching classpaths:

`clj -P`

- Start an nREPL server with the CIDER middleware:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}</span>`' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Start a REPL for ClojureScript and open a web browser:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}</span>`' --main cljs.main --repl`
