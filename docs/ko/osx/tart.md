---
layout: page
title: osx/tart (한국어)
description: "Apple Silicon에서 macOS 및 Linux 가상 머신(VM)을 빌드, 실행 및 관리."
content_hash: 2316f2c176a6983cdf8b35a1cd774fc87aebe664
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/tart.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/tart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tart

Apple Silicon에서 macOS 및 Linux 가상 머신(VM)을 빌드, 실행 및 관리.
더 많은 정보: <https://github.com/cirruslabs/tart>.

- 원격 VM 이미지 가져오기:

`tart pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acme.io/org/name:tag</span>

- 로컬 또는 원격 이미지 소스에서 VM 복제:

`tart clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스-VM</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>

- 특정 ipsw 파일에서 새로운 Mac VM 생성:

`tart create --from-ipsw=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest|경로/대상/파일.ipsw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>

- 기존 VM 실행:

`tart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>

- 특정 폴더를 마운트하여 기존 VM 실행:

`tart run --dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/로컬_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>

- VM 목록 나열:

`tart list`

- 실행 중인 VM의 IP 주소 확인:

`tart ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>

- VM의 디스플레이 해상도 변경:

`tart set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VM-이름</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>
