---
layout: page
title: common/ollama (English)
description: "A large language model runner."
content_hash: c2a27f4b126db0467620cf34ca076bdb6470633d
last_modified_at: 2024-04-12
tldri18n_status: 2
---
# ollama

A large language model runner.
More information: <https://github.com/jmorganca/ollama>.

- Start the daemon required to run other commands:

`ollama serve`

- Run a model and chat with it:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model</span>

- Run a model with a single prompt:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>

- List downloaded models:

`ollama list`

- Pull/Update a specific model:

`ollama pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model</span>

- Upgrade Ollama on Linux:

`curl -fsSL https://ollama.com/install.sh | sh`

- Delete a model:

`ollama rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model</span>

- Create a model from a `Modelfile`:

`ollama create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_model_name</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Modelfile</span>
