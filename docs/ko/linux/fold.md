---
layout: page
title: linux/fold (한국어)
description: "고정 폭 출력 장치를 위한 긴 줄을 접습니다."
content_hash: 3a93b90bd1899fafd64f5b19b7e4605e50236521
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fold.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/fold.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fold

고정 폭 출력 장치를 위한 긴 줄을 접습니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/fold>.

- 고정 폭으로 줄을 접기:

`fold --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폭</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 바이트 단위로 폭 계산 (기본값은 열 단위로 계산):

`fold --bytes --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_단위_폭</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 폭 제한 내에서 가장 오른쪽 공백 뒤에서 줄을 나누기:

`fold --spaces --width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">폭</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
