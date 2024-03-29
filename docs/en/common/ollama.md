---
layout: page
title: common/ollama (English)
description: "A large language model runner."
content_hash: 2ba55a3f170e46abd6db6fd5890308d150a8ecd1
last_modified_at: 2023-11-28
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

- Delete a model:

`ollama rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model</span>

- Create a model from a `Modelfile`:

`ollama create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_model_name</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Modelfile</span>
