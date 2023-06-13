---
layout: page
title: common/clj (English)
description: "Clojure tool to start a REPL or invoke a specific function with data."
content_hash: 111ff95f4ad6611b96d20401040ec8bcccd0056e
last_modified_at: 2023-06-13
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/clj.html
    icon: bi bi-globe
---
# clj

Clojure tool to start a REPL or invoke a specific function with data.
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
