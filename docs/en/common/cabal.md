---
layout: page
title: common/cabal (English)
description: "Command-line interface to the Haskell package infrastructure (Cabal)."
content_hash: 1dab5b7a4debc267fc8adc6d37243aec4dac3341
last_modified_at: 2024-05-23
related_topics:
  - title: italiano version
    url: /it/common/cabal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cabal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cabal.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cabal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cabal

Command-line interface to the Haskell package infrastructure (Cabal).
Manage Haskell projects and Cabal packages from the Hackage package repository.
More information: <https://cabal.readthedocs.io/en/latest/getting-started.html>.

- Search and list packages from Hackage:

`cabal list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Show information about a package:

`cabal info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Download and install a package:

`cabal install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Create a new Haskell project in the current directory:

`cabal init`

- Build the project in the current directory:

`cabal build`

- Run tests of the project in the current directory:

`cabal test`
