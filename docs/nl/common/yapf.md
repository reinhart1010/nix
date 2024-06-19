---
layout: page
title: common/yapf (Nederlands)
description: "Python stijlgidschecker."
content_hash: 7ee7f0687d89c623aded87f44916937ee7fdc69d
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/yapf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yapf

Python stijlgidschecker.
Meer informatie: <https://github.com/google/yapf>.

- Toon de geformateerde diff die zal optreden uit:

`yapf --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de geformateerde diff uit en breng de wijzigingen aan in het bestand:

`yapf --diff --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Formatteer alle Python-bestanden recursief in een map in parallel:

`yapf --recursive --in-place --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep8</span>` --parallel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
