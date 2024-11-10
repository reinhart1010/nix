---
layout: page
title: common/salt-call (한국어)
description: "로컬에서 salt minion에서 salt를 호출합니다."
content_hash: 273b51039c12cf8fd3fd08d1601ce1db0442a052
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/salt-call.html
    icon: bi bi-globe
tldri18n_status: 2
---
# salt-call

로컬에서 salt minion에서 salt를 호출합니다.
더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>.

- 이 minion에서 highstate 실행:

`salt-call state.highstate`

- highstate 시뮬레이션 실행, 모든 변경 사항을 계산하지만 실제로 수행하지 않음:

`salt-call state.highstate test=true`

- 자세한 디버깅 출력과 함께 highstate 실행:

`salt-call -l debug state.highstate`

- 이 minion의 grains 나열:

`salt-call grains.items`
