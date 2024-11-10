---
layout: page
title: common/shellcheck (한국어)
description: "쉘 스크립트를 정적으로 검사하여 오류, 사용 중단된/안전하지 않은 기능 및 잘못된 관행을 확인합니다."
content_hash: 55cb89e16d740ec13c916e365fd2190a660b5880
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/shellcheck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shellcheck

쉘 스크립트를 정적으로 검사하여 오류, 사용 중단된/안전하지 않은 기능 및 잘못된 관행을 확인합니다.
더 많은 정보: <https://github.com/koalaman/shellcheck/wiki>.

- 쉘 스크립트 검사:

`shellcheck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 스크립트 상단의 셰뱅을 무시하고 지정된 [s]쉘 방언으로 쉘 스크립트를 검사:

`shellcheck --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh|bash|dash|ksh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 하나 이상의 오류 유형을 무시:

`shellcheck --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SC1009,SC1073,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 소스된 쉘 스크립트도 검사:

`shellcheck --check-sourced `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 지정된 [f]포맷으로 출력 표시 (기본값은 `tty`):

`shellcheck --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty|checkstyle|diff|gcc|json|json1|quiet</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 하나 이상의 [o]선택적 검사 활성화:

`shellcheck --enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add-default-case,avoid-nullary-conditions,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>

- 기본적으로 비활성화된 모든 사용 가능한 선택적 검사 목록 나열:

`shellcheck --list-optional`

- 고려할 [S]심각도 수준 조정 (기본값은 `style`):

`shellcheck --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">error|warning|info|style</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.sh</span>
