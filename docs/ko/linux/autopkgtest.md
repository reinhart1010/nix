---
layout: page
title: linux/autopkgtest (한국어)
description: "Debian 패키지에 대한 테스트 실행."
content_hash: 81f5d4c8297c9c70efa553b29b60232cdb2c7e2e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/autopkgtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autopkgtest

Debian 패키지에 대한 테스트 실행.
더 많은 정보: <https://wiki.debian.org/ContinuousIntegration/autopkgtest>.

- 현재 디렉터리의 패키지를 빌드하고 모든 테스트를 시스템에서 직접 실행:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- 현재 디렉터리의 패키지에 대해 특정 테스트 실행:

`autopkgtest --test-name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- `apt-get`으로 특정 패키지를 다운로드 및 빌드한 후 모든 테스트 실행:

`autopkgtest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>

- 새로운 루트 디렉터리를 사용하여 현재 디렉터리의 패키지 테스트:

`autopkgtest -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chroot</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>

- 현재 디렉터리의 패키지를 재빌드하지 않고 테스트:

`autopkgtest --no-built-binaries -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">null</span>
