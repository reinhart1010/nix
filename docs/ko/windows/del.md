---
layout: page
title: windows/del (한국어)
description: "하나 이상의 파일 삭제."
content_hash: 49c8504b30efc11d1ede4351138eff965dec6504
last_modified_at: 2024-11-06
related_topics:
  - title: العربية version
    url: /ar/windows/del.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 2
---
# del

하나 이상의 파일 삭제.
PowerShell에서는 이 명령이 `Remove-Item`의 별칭입니다. 이 문서는 명령 프롬프트(`cmd`) 버전의 `del`을 기준으로 합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 동등한 PowerShell 명령의 문서 보기:

`tldr remove-item`

- 하나 이상의 파일 또는 패턴 삭제:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴1 파일_패턴2 ...</span>

- 각 파일을 삭제하기 전에 확인 요청:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` /p`

- 읽기 전용 파일 강제 삭제:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` /f`

- 모든 하위 디렉토리에서 파일을 재귀적으로 삭제:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` /s`

- 글로벌 와일드카드를 기반으로 파일 삭제 시 확인 요청 안 함:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` /q`

- 도움말 표시 및 사용 가능한 속성 목록 보기:

`del /?`

- 지정된 속성을 기반으로 파일 삭제:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성</span>
