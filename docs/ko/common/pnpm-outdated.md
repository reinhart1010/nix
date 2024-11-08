---
layout: page
title: common/pnpm-outdated (한국어)
description: "오래된 패키지 확인."
content_hash: e7ec27a59038bee9d7d0e6968ab8e937359e804b
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pnpm-outdated.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnpm outdated

오래된 패키지 확인.
인수를 제공하여 설치된 패키지의 일부 집합으로 확인을 제한할 수 있습니다 (패턴 지원).
더 많은 정보: <https://pnpm.io/cli/outdated>.

- 오래된 패키지 확인:

`pnpm outdated`

- 모든 워크스페이스 패키지에서 발견된 오래된 의존성 확인:

`pnpm outdated -r`

- 패키지 선택기를 사용하여 오래된 패키지 필터링:

`pnpm outdated --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_선택기</span>

- 오래된 패키지를 [g]lobal로 나열:

`pnpm outdated --global`

- 오래된 패키지의 세부정보 출력:

`pnpm outdated --long`

- 특정 형식으로 오래된 의존성 출력:

`pnpm outdated --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">형식</span>

- `package.json`의 사양을 충족하는 버전만 출력:

`pnpm outdated --compatible`

- 오래된 [D]ev 의존성만 확인:

`pnpm outdated --dev`
