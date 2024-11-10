---
layout: page
title: linux/pkgctl-build (한국어)
description: "깨끗한 `chroot` 환경에서 패키지를 빌드합니다."
content_hash: a15ae3a30fefada9cabe13f588dddeffd05ffae0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pkgctl-build.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pkgctl-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkgctl build

깨끗한 `chroot` 환경에서 패키지를 빌드합니다.
더 많은 정보: <https://manned.org/pkgctl-build.1>.

- 자동으로 올바른 빌드 스크립트를 선택하여 깨끗한 `chroot`에서 패키지 빌드:

`pkgctl build`

- 수동으로 깨끗한 `chroot`에서 패키지 빌드:

`pkgctl build --arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처</span>` --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>` --clean`
