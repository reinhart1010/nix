---
layout: page
title: linux/quickget (한국어)
description: "Quickemu 가상 머신 빌드를 위한 자료를 다운로드하고 준비합니다."
content_hash: 77e22747adc3e560851b61fd2aca1f1859ba0ed7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/quickget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# quickget

Quickemu 가상 머신 빌드를 위한 자료를 다운로드하고 준비합니다.
참고: "edition" 매개변수는 항상 선택 사항입니다.
같이 보기: `quickemu`.
더 많은 정보: <https://github.com/quickemu-project/quickemu>.

- 지원되는 모든 게스트 운영 체제, 버전 및 변형 목록 표시:

`quickget list`

- 운영 체제에 대한 Quickemu 가상 머신을 빌드하기 위한 가상 머신 설정 다운로드 및 생성:

`quickget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- VirtIO 드라이버가 포함된 Windows 11 VM 설정 다운로드:

`quickget windows 11`

- macOS 복구 이미지를 다운로드하고 가상 머신 설정 생성:

`quickget macos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mojave|catalina|big-sur|monterey|ventura|sonoma</span>

- 운영 체제의 ISO URL 표시:

`quickget --url fedora `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- 운영 체제에 대한 ISO 파일이 있는지 테스트:

`quickget --check nixos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- VM 설정을 빌드하지 않고 이미지 다운로드:

`quickget --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edition</span>

- 운영 체제 이미지에 대한 VM 설정 생성:

`quickget --create-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/iso</span>
