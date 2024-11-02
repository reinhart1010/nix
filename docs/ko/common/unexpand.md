---
layout: page
title: common/unexpand (한국어)
description: "공백을 탭으로 변환."
content_hash: a1b69d1b782151b8ba2c458c260cafcc86e0d5aa
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/unexpand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unexpand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unexpand

공백을 탭으로 변환.
더 많은 정보: <https://www.gnu.org/software/coreutils/unexpand>.

- 각 파일의 공백을 탭으로 변환하여 `stdout`에 출력:

`unexpand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdout`에서 읽어온 공백을 탭으로 변환:

`unexpand`

- 처음의 공백만이 아닌 모든 공백을 변환:

`unexpand -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 앞부분의 공백 시퀀스만 변환 (옵션 -a를 무시):

`unexpand --first-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 탭을 8칸이 아닌 지정한 문자 수만큼 떨어뜨려 변환 (-a 활성화):

`unexpand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
