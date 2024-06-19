---
layout: page
title: common/accelerate (Nederlands)
description: "Accelerate is een bibliotheek waarmee dezelfde PyTorch-code kan worden uitgevoerd op elke gedistribueerde configuratie."
content_hash: 8230d66a6ad42f2c1e47aaf5baee7f2ac38b1359
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/accelerate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Accelerate

Accelerate is een bibliotheek waarmee dezelfde PyTorch-code kan worden uitgevoerd op elke gedistribueerde configuratie.
Meer informatie: <https://huggingface.co/docs/accelerate/index>.

- Toon informatie over de omgeving:

`accelerate env`

- Maak interactief een configuratiebestand:

`accelerate config`

- Toon de geschatte GPU-geheugenkosten van het uitvoeren van een Hugging Face model met verschillende gegevenstypen:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name/model</span>

- Test een Accelerate configuratiebestand:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/config.yaml</span>

- Voer een model uit op CPU met Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Voer een model uit op multi-GPU met Accelerate, met 2 machines:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.py</span>` --multi_gpu --num_machines 2`
