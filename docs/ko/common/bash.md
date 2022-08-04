---
layout: page
title: common/bash (한국어)
description: "Bourne-Again SHell. `sh`-호환 명령 행 인터프리터."
content_hash: 40bc87d1c274c590d9dea2241e5c1f1a48fa78d5
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
---
# bash

Bourne-Again SHell. `sh`-호환 명령 행 인터프리터.
더 많은 정보: <https://gnu.org/software/bash/>.

- 대화식 쉘 시작:

`bash`

- 명령 실행:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- 파일에서 명령 실행:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- 파일에서 명령 실행하고, 터미널에서 실행 된 모든 명령 기록:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- 파일에서 명령 실행하고, 첫 번째 에러에서 중지:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- stdin에서 명령 실행:

`bash -s`

- bash의 버전 정보 출력 (`echo $BASH_VERSION`을 사용하여 버전 문자열만 표시):

`bash --version`
