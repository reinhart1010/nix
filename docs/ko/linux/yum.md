---
layout: page
title: linux/yum (한국어)
description: "RHEL, Fedora, CentOS(이전 버전용)를 위한 패키지 관리 도구."
content_hash: 4ec2810f1c3dd17be1ce930755724466dced0ca8
last_modified_at: 2024-10-29
related_topics:
  - title: català version
    url: /ca/linux/yum.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yum.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/yum.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/yum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/yum.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yum

RHEL, Fedora, CentOS(이전 버전용)를 위한 패키지 관리 도구.
다른 패키지 관리자의 동등한 명령을 보려면 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
더 많은 정보: <https://manned.org/yum>.

- 새 패키지 설치:

`yum install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 새 패키지를 설치하고 모든 질문에 대해 예로 가정 (업데이트에도 작동하며, 자동화된 업데이트에 유용):

`yum -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 명령을 제공하는 패키지 찾기:

`yum provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 패키지 제거:

`yum remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지에 대한 사용 가능한 업데이트 표시:

`yum check-update`

- 설치된 패키지를 최신 버전으로 업그레이드:

`yum upgrade`
