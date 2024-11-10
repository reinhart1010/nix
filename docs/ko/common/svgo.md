---
layout: page
title: common/svgo (한국어)
description: "SVG Optimizer: Scalable Vector Graphics 파일 최적화 도구. Node.js 기반."
content_hash: 43af289cb8bcdc09dc9bfa7d50c8771f4ef33cff
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/svgo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svgo

SVG Optimizer: Scalable Vector Graphics 파일 최적화 도구. Node.js 기반.
개별적으로 토글할 수 있는 일련의 변환 규칙(플러그인)을 적용합니다.
더 많은 정보: <https://github.com/svg/svgo>.

- 기본 플러그인을 사용하여 파일 최적화 (원본 파일을 덮어씁니다):

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트.svg</span>

- 파일을 최적화하고 결과를 다른 파일에 저장:

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트.min.svg</span>

- 디렉토리 내 모든 SVG 파일 최적화 (원본 파일을 덮어씁니다):

`svgo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더/안의/svg/파일들</span>

- 디렉토리 내 모든 SVG 파일을 최적화하고 결과 파일을 다른 디렉토리에 저장:

`svgo -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력/디렉토리/경로</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력/디렉토리/경로</span>

- 다른 명령에서 전달된 SVG 콘텐츠를 최적화하고 결과를 파일에 저장:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 테스트.svg</span>` | svgo -i - -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트.min.svg</span>

- 파일을 최적화하고 결과를 출력:

`svgo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트.svg</span>` -o -`

- 사용 가능한 플러그인 보기:

`svgo --show-plugins`
