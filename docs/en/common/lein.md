---
layout: page
title: common/lein (English)
description: "Manage Clojure projects with declarative configuration."
content_hash: 51222bac28b07dc068863cb5789c757678ecaa84
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# lein

Manage Clojure projects with declarative configuration.
More information: <https://leiningen.org>.

- Generate scaffolding for a new project based on a template:

`lein new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Start a REPL session either with the project or standalone:

`lein repl`

- Run the project's `-main` function with optional args:

`lein run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args</span>

- Run the project's tests:

`lein test`

- Package up the project files and all its dependencies into a jar file:

`lein uberjar`
