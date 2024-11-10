---
layout: page
title: common/tgpt (한국어)
description: "API 키가 필요 없는 AI 챗봇과 대화."
content_hash: 53298c80b38e124278390599a1d5e60dabbcb70d
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tgpt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tgpt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tgpt

API 키가 필요 없는 AI 챗봇과 대화.
사용 가능한 공급자: `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`.
더 많은 정보: <https://github.com/aandrew-me/tgpt>.

- 기본 공급자(GPT-3.5-turbo)와 대화:

`tgpt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- [m]ulti-line 대화형 모드 시작:

`tgpt --multiline`

- [i]mages 생성 후 현재 디렉토리에 저장:

`tgpt --image "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- 기본 공급자(GPT-3.5-turbo)로 [c]ode 생성:

`tgpt --code "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- 특정 공급자와 [q]uiet 모드(애니메이션 없이)로 대화:

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">openai|opengpts|koboldai|phind|llama2|blackboxai</span>` --quiet --whole "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- 특정 공급자를 사용하여 [s]hell 명령 생성 및 실행(확인 프롬프트 포함):

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">llama2</span>` --shell "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- API 키, 모델, 최대 응답 길이, 온도, `top_p`를 사용하여 프롬프트( `openai` 공급자를 사용할 때 필요):

`tgpt --provider openai --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">API_키</span>`" --model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-3.5-turbo</span>`" --max-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --temperature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>` --top_p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.9</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`"`

- 추가 사전 프롬프트 입력으로 파일 삽입:

`tgpt --provider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blackboxai</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
