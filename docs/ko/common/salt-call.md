---
layout: page
title: common/salt-call (한국어)
description: "로컬에서 salt minion에서 salt를 호출합니다."
content_hash: 273b51039c12cf8fd3fd08d1601ce1db0442a052
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/salt-call.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/salt-call.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># salt-call

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
