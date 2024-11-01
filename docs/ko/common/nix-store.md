---
layout: page
title: common/nix-store (한국어)
description: "Nix 저장소를 조작하거나 쿼리."
content_hash: de2f031f80c6a060d178273abbd8690271ae6100
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/nix-store.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nix-store.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nix-store

Nix 저장소를 조작하거나 쿼리.
같이 보기: `nix3 store`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/nix-store.html>.

- 사용하지 않는 경로를 제거하는 등의 쓰레기 수집:

`nix-store --gc`

- 동일한 파일을 하드 링크로 연결하여 공간 사용량 줄이기:

`nix-store --optimise`

- 특정 저장소 경로 삭제 (사용 중이지 않아야 함):

`nix-store --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- 저장소 경로(패키지)의 모든 의존성을 트리 형식으로 표시:

`nix-store --query --tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- 특정 저장소 경로와 모든 의존성의 총 크기 계산:

`du -cLsh $(nix-store --query --references `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>`)`

- 특정 저장소 경로에 대한 모든 종속 항목 표시:

`nix-store --query --referrers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>
