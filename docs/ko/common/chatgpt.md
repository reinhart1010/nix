---
layout: page
title: common/chatgpt (한국어)
description: "터미널에서 OpenAI의 ChatGPT 및 DALL-E를 사용하기 위한 쉘 스크립트."
content_hash: dbd3930754369c673a92e18e3a0331df1edbf112
last_modified_at: 2024-10-01
related_topics:
  - title: English version
    url: /en/common/chatgpt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chatgpt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chatgpt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chatgpt

터미널에서 OpenAI의 ChatGPT 및 DALL-E를 사용하기 위한 쉘 스크립트.
더 많은 정보: <https://github.com/0xacx/chatGPT-shell-cli>.

- 채팅 모드에서 시작:

`chatgpt`

- 다음 질문에 답하도록 프롬프트([p]rompt)를 제공:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일 주소와 일치하는 정규식은 무엇입니가?</span>`"`

- 특정 모델([m]odel)을 사용하여 채팅 모드에서 시작(기본값은 `gpt-3.5-turbo`입니다):

`chatgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-4</span>

- 초기([i]nitial) 프롬프트로 채팅 모드를 시작:

`chatgpt --init-prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">당신은 Rick과 Morty의 Rick입니다. 그의 매너리즘을 사용하여 질문에 응답하고 모욕적인 농담을 포함합니다.</span>`"`

- 명령 결과를 `chatgpt`에 프롬프트로 파이프:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ubuntu에서 실행중인 프로세스를 보는 방법?</span>`" | chatgpt`

- DALL-E를 사용하여 이미지를 생성:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image: A white cat</span>`"`
