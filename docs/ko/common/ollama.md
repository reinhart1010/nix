---
layout: page
title: common/ollama (한국어)
description: "대규모 언어 모델 실행기."
content_hash: 50dc4a2e2d53f22f47032b56faec34060ecfb700
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ollama.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ollama.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ollama.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ollama

대규모 언어 모델 실행기.
사용 가능한 모델 목록은 <https://ollama.com/library>를 참조하세요.
더 많은 정보: <https://github.com/ollama/ollama>.

- 다른 명령을 실행하는 데 필요한 데몬 시작:

`ollama serve`

- 모델을 실행하고 대화:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델</span>

- 단일 프롬프트로 모델 실행:

`ollama run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>

- 다운로드된 모델 나열:

`ollama list`

- 특정 모델 가져오기/업데이트:

`ollama pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델</span>

- 실행 중인 모델 나열:

`ollama ps`

- 모델 삭제:

`ollama rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델</span>

- `Modelfile`로부터 모델 생성:

`ollama create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_모델_이름</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/Modelfile</span>
