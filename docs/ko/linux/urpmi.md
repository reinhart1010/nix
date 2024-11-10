---
layout: page
title: linux/urpmi (한국어)
description: "Mageia에서 패키지를 설치합니다."
content_hash: 9844e15bd7c8835cafad4687aafd2aa8c8a9d467
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/urpmi.html
    icon: bi bi-globe
tldri18n_status: 2
---
# urpmi

Mageia에서 패키지를 설치합니다.
같이 보기: `urpm.update`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpmi>.

- 저장소 또는 로컬 RPM 파일에서 패키지 설치:

`sudo urpmi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지|경로/대상/파일.rpm</span>

- 패키지를 다운로드만 하고 설치하지 않음:

`urpmi --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지 업데이트 (`urpmi.update -a`를 실행하여 사용 가능한 업데이트 확인):

`sudo urpmi --auto-select`

- 네트워크의 하나 이상의 머신에서 `/etc/urpmi/parallel.cfg`에 따라 패키지 업데이트:

`sudo urpmi --parallel local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 모든 고아 패키지를 수동으로 설치됨으로 표시:

`sudo urpmi $(urpmq --auto-orphans -f)`
