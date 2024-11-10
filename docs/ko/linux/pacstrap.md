---
layout: page
title: linux/pacstrap (한국어)
description: "Arch Linux 설치 스크립트로, 지정된 새로운 루트 디렉터리에 패키지를 설치합니다."
content_hash: 49ad67dfdfd34c52eef211cd60b56c1eca4a00bc
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pacstrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacstrap

Arch Linux 설치 스크립트로, 지정된 새로운 루트 디렉터리에 패키지를 설치합니다.
더 많은 정보: <https://manned.org/pacstrap.8>.

- `base` 패키지, 리눅스 커널 및 일반 하드웨어용 펌웨어 설치:

`pacstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux-firmware</span>

- `base` 패키지, 리눅스 LTS 커널 및 `base-devel` 빌드 도구 설치:

`pacstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base-devel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linux-lts</span>

- 호스트의 미러리스트를 대상에 복사하지 않고 패키지 설치:

`pacstrap -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지들</span>

- Pacman의 대체 설정 파일 사용:

`pacstrap -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pacman.conf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지들</span>

- 대상이 아닌 호스트의 패키지 캐시를 사용하여 패키지 설치:

`pacstrap -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지들</span>

- 호스트에서 복사하지 않고 대상에서 빈 `pacman` 키링 초기화:

`pacstrap -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지들</span>

- 대화형 모드로 패키지 설치 (확인 요청):

`pacstrap -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지들</span>

- 패키지 파일을 사용하여 패키지 설치:

`pacstrap -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지2</span>
