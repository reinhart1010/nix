---
layout: page
title: common/openai (English)
description: "CLI tool providing access to the OpenAI API."
content_hash: a145145be9fafaa9ef437f3700baebc502b7fdad
last_modified_at: 2023-03-03
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># openai

CLI tool providing access to the OpenAI API.
More information: <https://github.com/openai/openai-python>.

- List models:

`openai api models.list`

- Create a completion:

`openai api completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ada</span>` --prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Hello world"</span>

- Create a chat completion:

`openai api chat_completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>` --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user "Hello world"</span>

- Generate images via DALL·E API:

`openai api image.create --prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"two dogs playing chess, cartoon"</span>` --num-images `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
