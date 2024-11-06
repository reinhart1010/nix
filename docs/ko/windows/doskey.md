---
layout: page
title: windows/doskey (한국어)
description: "매크로, Windows 명령 및 명령줄을 관리합니다."
content_hash: 968649b6d757c006c6b345fce5df039b1db2e6f2
last_modified_at: 2024-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/doskey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/doskey.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/doskey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/doskey.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/doskey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doskey

매크로, Windows 명령 및 명령줄을 관리합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- 사용 가능한 매크로 나열:

`doskey /macros`

- 새 매크로 생성:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 특정 실행 파일에 대한 새 매크로 생성:

`doskey /exename=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">실행파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`"`

- 매크로 제거:

`doskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` =`

- 메모리에 저장된 모든 명령 표시:

`doskey /history`

- 매크로를 파일에 저장하여 휴대성 확보:

`doskey /macros > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\macinit_파일</span>

- 파일에서 매크로 로드:

`doskey /macrofile = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\macinit_파일</span>
