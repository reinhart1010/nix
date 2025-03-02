---
layout: page
title: common/uname (한국어)
description: "현재 컴퓨터와 그 컴퓨터에서 실행 중인 운영 체제에 대한 세부 정보를 출력합니다."
content_hash: 15b5bc8fd516fbb7913e2762e07f16c0d2b679f8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/uname.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/uname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/uname.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/uname.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/uname.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/uname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uname

현재 컴퓨터와 그 컴퓨터에서 실행 중인 운영 체제에 대한 세부 정보를 출력합니다.
`lsb_release`로 같이 참고해주세요.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html>.

- 커널 이름 출력:

`uname`

- 시스템 아키텍처 및 프로세서 정보 출력:

`uname --machine --processor`

- 커널 이름, 커널 릴리스 및 버전 출력:

`uname --kernel-name --kernel-release --kernel-version`

- 시스템 호스트 이름 출력:

`uname --nodename`

- 사용 가능한 모든 시스템 정보를 출력:

`uname --all`
