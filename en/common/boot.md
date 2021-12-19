---
layout: page
title: common/boot (English)
description: "Build tooling for the Clojure programming language."
content_hash: a7eb28445c2203022c0b0a25a21b16f20e90149b
related_topics:
  - title: italiano version
    url: /it/common/boot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/boot.html
    icon: bi bi-globe
---
# boot

Build tooling for the Clojure programming language.
More information: <https://github.com/boot-clj/boot>.

- Start a REPL session either with the project or standalone:

`boot repl`

- Build a single `uberjar`:

`boot jar`

- Learn about a command:

`boot cljs --help`

- Generate scaffolding for a new project based on a template:

`boot --dependencies boot/new new --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template_name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Build for development (if using the boot/new template):

`boot dev`

- Build for production (if using the boot/new template):

`boot prod`
