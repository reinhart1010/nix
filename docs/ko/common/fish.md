---
layout: page
title: common/fish (한국어)
description: "사용자 친화적으로 설계된 명령줄 해석기인 Friendly Interactive SHell입니다."
content_hash: 3b4ee734e8d770d84c3d3ae348b364113718c3d3
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/fish.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fish.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fish.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fish

사용자 친화적으로 설계된 명령줄 해석기인 Friendly Interactive SHell입니다.
더 많은 정보: <https://fishshell.com>.

- 대화형 쉘 세션을 시작:

`fish`

- 시작 구성을 로드하지 않고 대화형 쉘 세션을 시작:

`fish --no-config`

- 특정 명령을 실행:

`fish --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'fish is executed'</span>`"`

- 특정 스크립트를 실행:

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.fish</span>

- 구문 오류가 있는지 특정 스크립트를 확인:

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.fish</span>

- `stdin`에서 특정 명령을 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'fish is executed'"</span>` | fish`

- 쉘이 이전 기록에 액세스하거나 새 기록을 저장하지 않는 비공개 모드에서 대화형 쉘 세션을 시작:

`fish --private`

- 쉘을 다시 시작해도 지속되는 환경 변수를 정의하고 내보냄 (기본 제공):

`set --universal --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_값</span>
