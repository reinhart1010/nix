---
layout: page
title: common/sgpt (한국어)
description: "OpenAI의 GPT 모델로 구동되는 명령줄 생산성 도구."
content_hash: de4ba2f06f38caa0f979780b7096d59fa31df382
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sgpt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sgpt

OpenAI의 GPT 모델로 구동되는 명령줄 생산성 도구.
더 많은 정보: <https://github.com/TheR1D/shell_gpt#readme>.

- 검색 엔진으로 사용하여 태양의 질량을 묻기:

`sgpt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태양의 질량</span>`"`

- 쉘 명령 실행, 현재 디렉토리의 모든 파일에 `chmod 444` 적용:

`sgpt --shell "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재 디렉토리의 모든 파일을 읽기 전용으로 설정</span>`"`

- 코드 생성, 클래식한 fizz buzz 문제 해결:

`sgpt --code "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Python을 사용하여 fizz buzz 문제 해결</span>`"`

- 고유한 세션 이름으로 채팅 세션 시작:

`sgpt --chat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내가 좋아하는 숫자를 기억해 주세요: 4</span>`"`

- `REPL` (Read–eval–print loop) 세션 시작:

`sgpt --repl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 도움말 표시:

`sgpt --help`
