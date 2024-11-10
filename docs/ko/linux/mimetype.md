---
layout: page
title: linux/mimetype (한국어)
description: "파일의 MIME 유형을 자동으로 결정합니다."
content_hash: 03958a6c0849fb2f995a0fb7cad271d42af5d196
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mimetype.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mimetype

파일의 MIME 유형을 자동으로 결정합니다.
더 많은 정보: <https://manned.org/mimetype>.

- 주어진 파일의 MIME 유형 출력:

`mimetype `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일명을 제외하고 MIME 유형만 표시:

`mimetype --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- MIME 유형 설명 표시:

`mimetype --describe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`의 MIME 유형 결정 (파일명 확인하지 않음):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | mimetype --stdin`

- MIME 유형이 결정된 방법에 대한 디버그 정보 표시:

`mimetype --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 파일의 가능한 모든 MIME 유형을 신뢰도 순으로 표시:

`mimetype --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력의 2글자 언어 코드를 명시적으로 지정:

`mimetype --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
