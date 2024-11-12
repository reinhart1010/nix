---
layout: page
title: linux/spectre-meltdown-checker (한국어)
description: "Spectre와 Meltdown 완화 감지 도구."
content_hash: d2e5ac606778a482db7319e45405a44326dbc23d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/spectre-meltdown-checker.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spectre-meltdown-checker

Spectre와 Meltdown 완화 감지 도구.
더 많은 정보: <https://manned.org/spectre-meltdown-checker>.

- 현재 실행 중인 커널을 Spectre 또는 Meltdown에 대해 검사:

`sudo spectre-meltdown-checker`

- 현재 실행 중인 커널을 검사하고 취약성을 완화하기 위한 조치 설명 표시:

`sudo spectre-meltdown-checker --explain`

- 특정 변종 검사 (기본적으로 모두 검사):

`sudo spectre-meltdown-checker --variant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds</span>

- 특정 출력 형식을 사용하여 출력 표시:

`sudo spectre-meltdown-checker --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|json|nrpe|prometheus|short</span>

- `/sys` 인터페이스가 존재해도 사용하지 않음:

`sudo spectre-meltdown-checker --no-sysfs`

- 실행 중이지 않은 커널 검사:

`sudo spectre-meltdown-checker --kernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/커널_파일</span>
