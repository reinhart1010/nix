---
layout: page
title: windows/fondue (한국어)
description: "선택적 Windows 기능 설치."
content_hash: 0f09ccd2a45182571e712f6199e1241e79d20c11
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/fondue.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/fondue.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/fondue.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fondue

선택적 Windows 기능 설치.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/fondue>.

- 특정 Windows 기능 활성화:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>

- 사용자에게 모든 출력 메시지 숨기기:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>` /hide-ux:all`

- 오류 보고를 위한 호출자 프로세스 이름 지정:

`fondue /enable-feature:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능</span>` /caller-name:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
