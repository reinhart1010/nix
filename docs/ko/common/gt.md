---
layout: page
title: common/gt (한국어)
description: "Git 및 GitHub에 대한 종속 코드 변경(스택) 시퀀스를 생성하고 관리."
content_hash: be5a1bcb99277d4cf1431f1b80c88652709ee188
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gt

Git 및 GitHub에 대한 종속 코드 변경(스택) 시퀀스를 생성하고 관리.
더 많은 정보: <https://docs.graphite.dev>.

- Graphite의 API를 사용하여 CLI 인증:

`gt auth --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">graphite_cli_인증_토큰</span>

- 현재 디렉터리의 저장소에 대해 `gt`를 초기화:

`gt repo init`

- 현재 브랜치 위에 쌓은 새로운 브랜치를 만들고 단계적 변경 사항을 커밋:

`gt branch create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 새로운 커밋을 생성하고 업스택 브랜치를 수정:

`gt commit create -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_메시지</span>

- 현재 스택의 모든 브랜치를 GitHub에 강제로 푸시하고 PR을 생성하거나 업데이트:

`gt stack submit`

- 추적된 모든 스택을 기록:

`gt log short`

- 지정된 하위 명령에 대한 도움말을 표시:

`gt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>` --help`
