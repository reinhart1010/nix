---
layout: page
title: common/elm (English)
description: "Compile and run Elm source files."
content_hash: 420d212353f8d0f87dc3baba4c0aba27f28ee4c3
last_modified_at: 2023-09-10
related_topics:
  - title: italiano version
    url: /it/common/elm.html
    icon: bi bi-globe
---
# elm

Compile and run Elm source files.
More information: <https://elm-lang.org>.

- Initialize an Elm project, generates an elm.json file:

`elm init`

- Start interactive Elm shell:

`elm repl`

- Compile an Elm file, output the result to an `index.html` file:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>

- Compile an Elm file, output the result to a JavaScript file:

`elm make `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>`.js`

- Start local web server that compiles Elm files on page load:

`elm reactor`

- Install Elm package from <https://package.elm-lang.org>:

`elm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
