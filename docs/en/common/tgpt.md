---
layout: page
title: common/tgpt (English)
description: "Talk to an AI chatbot without the need for API keys."
content_hash: 8e30c4f0f81a79fc0017dd40d17eeeebd612705b
last_modified_at: 2024-02-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tgpt

Talk to an AI chatbot without the need for API keys.
Available providers: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
More information: <https://github.com/aandrew-me/tgpt>.

- Chat with the default provider (GPT-3.5-turbo):

`tgpt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Start [m]ulti-line interactive mode:

`tgpt --multiline`

- Generate [i]mages and save them to the current directory:

`tgpt --image "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Generate [c]ode with the default provider (GPT-3.5-turbo):

`tgpt --code "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Chat with a specific provider [q]uietly (without animations):

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openai|opengpts|koboldai|phind|llama2|blackboxai</span>` --quiet --whole "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Generate and execute [s]hell commands using a specific provider (with a confirmation prompt):

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">llama2</span>` --shell "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Prompt with an API key, model, max response length, temperature, and `top_p` (required when using `openai` provider):

`tgpt --provider openai --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_key</span>`" --model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>`" --max-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --temperature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>` --top_p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`"`

- Feed a file as additional pre-prompt input:

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blackboxai</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
