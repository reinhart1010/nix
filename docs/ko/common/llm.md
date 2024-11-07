---
layout: page
title: common/llm (한국어)
description: "원격 API 및 로컬에서 설치 및 실행할 수 있는 모델을 통해 대형 언어 모델(LLM)과 상호 작용."
content_hash: 695d103c9a8223693f582afbc21a2233c30528ca
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/llm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llm

원격 API 및 로컬에서 설치 및 실행할 수 있는 모델을 통해 대형 언어 모델(LLM)과 상호 작용.
더 많은 정보: <https://llm.datasette.io/en/stable/help.html>.

- OpenAI API 키 설정:

`llm keys set openai`

- 프롬프트 실행:

`llm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">펠리칸 애완동물에게 어울리는 재미있는 이름 10개</span>`"`

- 파일에 대해 [s]시스템 프롬프트 실행:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>` | llm --system "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이 코드를 설명하세요</span>`"`

- LLM과 동일한 환경에 PyPI에서 패키지 설치:

`llm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지1 패키지2 ...</span>

- [m]모델을 다운로드하고 프롬프트 실행:

`llm --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">orca-mini-3b-gguf2-q4_0</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프랑스의 수도는 어디인가요?</span>`"`

- [s]시스템 프롬프트를 생성하고 템플릿 이름으로 [s]저장:

`llm --system '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">당신은 지각 있는 치즈케이크입니다</span>`' --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지각있는_치즈케이크</span>

- 특정 [m]모델과 특정 [t]템플릿을 사용하여 대화형 채팅:

`llm chat --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chatgpt</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지각있는_치즈케이크</span>
