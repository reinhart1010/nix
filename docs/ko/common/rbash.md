---
layout: page
title: common/rbash (한국어)
description: "제한된 Bash 셸로, `bash --restricted`와 동등합니다."
content_hash: ac18bd35735838d966ee784948ed3da253ed5f6d
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rbash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rbash

제한된 Bash 셸로, `bash --restricted`와 동등합니다.
작업 디렉토리 변경, 명령 출력 리디렉션, 환경 변수 수정 등을 허용하지 않습니다.
히스토리 확장을 위해 `histexpand`도 참조하세요.
더 많은 정보: <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>.

- 대화형 셸 세션 시작:

`rbash`

- 명령을 실행한 후 종료:

`rbash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 스크립트 실행:

`rbash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 각 명령을 실행 전에 출력하며 스크립트 실행:

`rbash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 스크립트에서 명령을 읽고 첫 번째 오류에서 중지:

`rbash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- `stdin`에서 명령을 읽고 실행:

`rbash -s`
