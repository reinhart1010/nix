---
layout: page
title: common/accelerate (English)
description: "A library that enables the same PyTorch code to be run across any distributed configuration."
content_hash: 86d1e1be4f4eac737a4f0769d8166dd810ddbe06
last_modified_at: 2024-07-11
related_topics:
  - title: Indonesia version
    url: /id/common/accelerate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/accelerate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/accelerate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/accelerate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# accelerate

A library that enables the same PyTorch code to be run across any distributed configuration.
More information: <https://huggingface.co/docs/accelerate/index>.

- Print environment information:

`accelerate env`

- Interactively create a configuration file:

`accelerate config`

- Print the estimated GPU memory cost of running a Hugging Face model with different data types:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name/model</span>

- Test an Accelerate configuration file:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>

- Run a model on CPU with Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Run a model on multi-GPU with Accelerate, with 2 machines:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>` --multi_gpu --num_machines 2`
