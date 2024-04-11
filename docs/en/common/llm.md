---
layout: page
title: common/llm (English)
description: "Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine."
content_hash: cd89a65c6e0b48f420a0f8e642a25448ee06b0ac
last_modified_at: 2024-04-11
tldri18n_status: 2
---
# llm

Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine.
More information: <https://llm.datasette.io/en/stable/help.html>.

- Set up an OpenAI API Key:

`llm keys set openai`

- Run a prompt:

`llm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ten fun names for a pet pelican</span>`"`

- Run a [s]ystem prompt against a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>` | llm --system "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Explain this code</span>`"`

- Install packages from PyPI into the same environment as LLM:

`llm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- Download and run a prompt against a [m]odel:

`llm --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">orca-mini-3b-gguf2-q4_0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">What is the capital of France?</span>`"`

- Create a [s]ystem prompt and [s]ave it with a template name:

`llm --system '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">You are a sentient cheesecake</span>`' --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sentient_cheesecake</span>

- Have an interactive chat with a specific [m]odel using a specific [t]emplate:

`llm chat --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chatgpt</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sentient_cheesecake</span>
