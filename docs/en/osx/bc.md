---
layout: page
title: osx/bc (English)
description: "An arbitrary precision calculator language."
content_hash: ecf5940be267eb6ec80441aed8d53eccbdbbc0e0
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bc

An arbitrary precision calculator language.
See also: `dc`.
More information: <https://manned.org/man/freebsd-13.0/bc.1>.

- Start an interactive session:

`bc`

- Start an interactive session with the standard math library enabled:

`bc --mathlib`

- Calculate an expression:

`bc --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Execute a script:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.bc</span>

- Calculate an expression with the specified scale:

`bc --expression='scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`'`

- Calculate a sine/cosine/arctangent/natural logarithm/exponential function using `mathlib`:

`bc --mathlib --expression='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)'`
