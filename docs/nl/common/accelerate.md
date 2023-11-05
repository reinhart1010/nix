---
layout: page
title: common/accelerate (Nederlands)
description: "Accelerate is een bibliotheek waarmee dezelfde PyTorch-code kan worden uitgevoerd op elke gedistribueerde configuratie."
content_hash: 9e47de7e9131fe9325c0a07b0d51a6d274ceaa70
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Accelerate

Accelerate is een bibliotheek waarmee dezelfde PyTorch-code kan worden uitgevoerd op elke gedistribueerde configuratie.
Meer informatie: <https://huggingface.co/docs/accelerate/index>.

- Toon informatie over de omgeving:

`accelerate env`

- Maak interactief een configuratiebestand:

`accelerate config`

- Druk de geschatte GPU-geheugenkosten af van het uitvoeren van een huggingface model met verschillende gegevenstypen:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name/model</span>

- Test een Accelerate configuratiebestand:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/config.yaml</span>

- Voer een model uit op CPU met Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Voer een model uit op multi-GPU met Accelerate, met 2 machines:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.py</span>` --multi_gpu --num_machines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
