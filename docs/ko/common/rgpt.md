---
layout: page
title: common/rgpt (한국어)
description: "터미널에서 바로 사용할 수 있는 GPT 기반 자동 코드 리뷰 도구."
content_hash: 78d9e9591aa6fc30ee992b91038d8c6c0b7a0f00
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rgpt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rgpt

터미널에서 바로 사용할 수 있는 GPT 기반 자동 코드 리뷰 도구.
더 많은 정보: <https://github.com/vibovenkat123/review-gpt>.

- 추가 옵션 없이 GPT에게 코드 개선 요청:

`rgpt --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`

- 코드 리뷰 중 `rgpt`에서 더 자세한 출력 얻기:

`rgpt --v --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`

- GPT에게 코드 개선 요청 및 GPT3 토큰 수를 특정 수로 제한하기:

`rgpt --max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`

- 0에서 2 사이의 실수값을 사용하여 더 독특한 결과 요청 (높을수록 더 독특함):

`rgpt --pres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`

- 특정 모델을 사용하여 코드 리뷰 요청:

`rgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">davinci</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`

- `rgpt`를 사용하여 JSON 출력 생성:

`rgpt --json --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>`)"`
