---
layout: page
title: common/clj (Nederlands)
description: "Clojure tool om een REPL te starten of roep een een specifieke functie aan met data."
content_hash: eca67d312a2a821ff98f4d5c26aeae28144cd107
last_modified_at: 2023-12-10
related_topics:
  - title: English version
    url: /en/common/clj.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clj.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clj

Clojure tool om een REPL te starten of roep een een specifieke functie aan met data.
Alle opties kunnen worden gedefinieerd in een `deps.edn` bestand.
Meer informatie: <https://clojure.org/guides/deps_and_cli>.

- Start een REPL (interactieve shell):

`clj`

- Voer een functie uit:

`clj -X `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace/functie_naam</span>

- Voer de voornaamste functie uit van een gespecificeerde namespace:

`clj -M -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

- Bereid een project voor door afhankelijkheden op te lossen, het downloaden van bibliotheken en het maken/cachen van classpaths:

`clj -P`

- Start een nREPL server met de CIDER middleware:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}</span>`' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Start een REPL voor ClojureScript en open een web browser:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}</span>`' --main cljs.main --repl`
