---
layout: page
title: linux/navi (한국어)
description: "명령줄 및 애플리케이션 실행기를 위한 대화형 치트시트 도구."
content_hash: 095078a87b292c9e9fa41fb73670f43799dbfd9c
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/navi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# navi

명령줄 및 애플리케이션 실행기를 위한 대화형 치트시트 도구.
더 많은 정보: <https://github.com/denisidoro/navi>.

- 사용 가능한 모든 치트시트를 탐색:

`navi`

- `navi` 자체에 대한 치트시트를 탐색:

`navi fn welcome`

- 치트시트에서 명령어를 실행하지 않고 출력:

`navi --print`

- 셸 위젯 소스 코드 출력 (가능한 경우 자동으로 셸을 감지하지만, 수동으로 지정할 수도 있음):

`navi widget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">셸</span>

- 쿼리에 가장 잘 맞는 스니펫을 자동 선택 및 실행:

`navi --query '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>`' --best-match`
