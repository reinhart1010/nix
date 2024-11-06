---
layout: page
title: windows/choice (한국어)
description: "사용자에게 선택지를 제시하고 선택한 선택지의 색인을 반환합니다."
content_hash: ea13c2f3bc817c49150a5c22c771a93f8a8e94e1
last_modified_at: 2024-11-06
related_topics:
  - title: বাংলা version
    url: /bn/windows/choice.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choice.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choice

사용자에게 선택지를 제시하고 선택한 선택지의 색인을 반환합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/choice>.

- 현재 사용자에게 `Y` 또는 `N` 선택지를 제시:

`choice`

- 현재 사용자에게 특정 세트에서 [c]hoice 선택지를 제시:

`choice /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AB</span>

- 현재 사용자에게 특정 [m]essage와 함께 선택지를 제시:

`choice /m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 현재 사용자에게 대소문자를 구분하는 [c]ase-[s]ensitive [c]hoice 선택지를 특정 세트에서 제시:

`choice /cs /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Ab</span>

- 현재 사용자에게 선택지를 제시하고, 특정 [t]ime 내에 [d]efault 선택지를 선호:

`choice /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- 도움말 표시:

`choice /?`
