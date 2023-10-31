---
layout: page
title: common/accelerate (English)
description: "Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration."
content_hash: 81d3914bea3185639fe0264a3cc82880cf994a3e
last_modified_at: 2023-10-31
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Accelerate

Accelerate is a library that enables the same PyTorch code to be run across any distributed configuration.
More information: <https://huggingface.co/docs/accelerate/index>.

- Print environment information:

`accelerate env`

- Interactively create a configuration file:

`accelerate config`

- Print the estimated GPU memory cost of running a huggingface model with different data types:

`accelerate estimate-memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name/model</span>

- Test an Accelerate configuration file:

`accelerate test --config_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>

- Run a model on CPU with Accelerate:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cpu</span>

- Run a model on multi-GPU with Accelerate, with 2 machines:

`accelerate launch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>` --multi_gpu --num_machines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
