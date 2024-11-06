---
layout: page
title: common/openai (한국어)
description: "OpenAI API에 접근할 수 있는 CLI 도구."
content_hash: d47f7bd4c0be2efef1c58f486b00abaf2546a723
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/openai.html
    icon: bi bi-globe
tldri18n_status: 2
---
# openai

OpenAI API에 접근할 수 있는 CLI 도구.
더 많은 정보: <https://github.com/openai/openai-python>.

- 모델 나열:

`openai api models.list`

- 완료 생성:

`openai api completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ada</span>` --prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Hello world"</span>

- 채팅 완료 생성:

`openai api chat_completions.create --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>` --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user "Hello world"</span>

- DALL·E API를 통해 이미지 생성:

`openai api image.create --prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"two dogs playing chess, cartoon"</span>` --num-images `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
