---
layout: page
title: common/yapf (Nederlands)
description: "Python stijlgidschecker."
content_hash: 06f8aef5f6df4328a7af98dd2ff1564a6bc2778b
related_topics:
  - title: English version
    url: /en/common/yapf.html
    icon: bi bi-globe
---
# yapf

Python stijlgidschecker.
Meer informatie: <https://github.com/google/yapf>.

- Print de geformateerde diff die zal optreden uit:

`yapf --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Print de geformateerde diff uit en breng de wijzigingen aan in het bestand:

`yapf --diff --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Formatteer alle Python-bestanden recursief in een map in parallel:

`yapf --recursive --in-place --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep8</span>` --parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
