---
layout: page
title: linux/urpmi.update (한국어)
description: "Mageia에서 패키지 저장소의 패키지 목록을 업데이트합니다."
content_hash: 5e8803980140f18afb15343ef6bebfe6e9520d80
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/urpmi.update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# urpmi.update

Mageia에서 패키지 저장소의 패키지 목록을 업데이트합니다.
참고: Mageia 문서에서는 medium과 저장소를 동의어로 사용합니다.
같이 보기: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpmi.update>.

- 모든 활성 미디어 업데이트:

`urpmi.update -a`

- 특정 미디어 업데이트 (비활성 미디어 포함):

`urpmi.update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미디어1 미디어2 ...</span>

- 특정 키워드를 포함하는 모든 미디어 업데이트:

`urpmi.update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 모든 구성된 미디어 업데이트:

`urpmi.update e`
