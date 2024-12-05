---
layout: page
title: common/openai (English)
description: "CLI tool providing access to the OpenAI API."
content_hash: 1e4f9a08befe27670b7526a05c274b10e69092df
last_modified_at: 2024-12-05
related_topics:
  - title: 한국어 version
    url: /ko/common/openai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openai

CLI tool providing access to the OpenAI API.
More information: <https://github.com/openai/openai-python>.

- List models:

`openai api models.list`

- Create a completion:

`openai api completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ada</span>` --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello world</span>`"`

- Create a chat completion:

`openai api chat_completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>` --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user "Hello world"</span>

- Generate images via DALL·E API:

`openai api image.create --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">two dogs playing chess, cartoon</span>`" --num-images `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
