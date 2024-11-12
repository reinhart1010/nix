---
layout: page
title: osx/spctl (한국어)
description: "보안 평가 정책 하위 시스템 관리."
content_hash: f25ca09ae693daef1749a12de2ca9b4795220872
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/spctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/spctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# spctl

보안 평가 정책 하위 시스템 관리.
macOS에서 Gatekeeper를 관리하는 도구.
더 많은 정보: <https://keith.github.io/xcode-man-pages/spctl.8.html>.

- Gatekeeper 비활성화:

`spctl --master-disable`

- 애플리케이션 실행을 허용하는 규칙 추가 (규칙의 라벨 지정은 선택 사항):

`spctl --add --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Gatekeeper 활성화:

`spctl --master-enable`

- 시스템의 모든 규칙 나열:

`spctl --list`
