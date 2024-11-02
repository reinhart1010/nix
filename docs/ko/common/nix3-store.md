---
layout: page
title: common/nix3-store (한국어)
description: "Nix 저장소를 조작."
content_hash: 0597cb596ecbacdf84c20eb7b0df560b85587b6c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/nix3-store.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nix store

Nix 저장소를 조작.
같이 보기: `nix-store`.
더 많은 정보: <https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-store.html>.

- 가비지 수집을 통해 공간 사용량 줄이기 위해 사용되지 않는 경로 제거:

`nix store gc`

- 동일한 파일을 하드링크하여 공간 사용량 줄이기:

`nix store optimise`

- 특정 저장소 경로 삭제 (사용되지 않아야 함):

`nix store delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- 원격 저장소의 경로 내용을 나열:

`nix store --store `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://cache.nixos.org</span>` ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>

- 두 저장소 경로 간의 버전 차이와 해당 종속성 표시:

`nix store diff-closures `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/nix/store/...</span>
