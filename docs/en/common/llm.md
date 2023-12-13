---
layout: page
title: common/llm (English)
description: "Interact with Large Language Models (LLMs) via remote APIs and models that can be installed and run on your machine."
content_hash: 4bec98769de046eff803497b451e1e1d05b0b19a
last_modified_at: 2023-12-13
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llm

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

- Have an interactive chat with a specific [m]odel:

`llm chat --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chatgpt</span>
