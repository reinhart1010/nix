---
layout: page
title: windows/gcrane-completion (한국어)
description: "gcrane에 대한 자동 완성 스크립트를 생성합니다."
content_hash: d33d7e4dabc8058f695c4fe02cbf8d491d750017
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/gcrane-completion.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/gcrane-completion.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane completion

gcrane에 대한 자동 완성 스크립트를 생성합니다.
사용 가능한 쉘은 `bash`, `fish`, `powershell`, 및 `zsh`입니다.
더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- 쉘에 대한 자동 완성 스크립트 생성:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쉘_이름</span>

- 자동 완성 설명 비활성화:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쉘_이름</span>` --no-descriptions`

- 현재 쉘 세션에 자동 완성 로드 (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- 새 세션에 대한 자동 완성 로드 (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- 도움말 표시:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쉘_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
