---
layout: page
title: linux/zenity (한국어)
description: "명령줄/셸 스크립트에서 대화 상자를 표시."
content_hash: 3ec5ea9adcc13ecaec2e322768d2ccc59ee9dd49
last_modified_at: 2024-10-28
related_topics:
  - title: English version
    url: /en/linux/zenity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/zenity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zenity

명령줄/셸 스크립트에서 대화 상자를 표시.
사용자 입력 값을 반환하거나 오류 시 1을 반환.
더 많은 정보: <https://manned.org/zenity>.

- 기본 질문 대화 상자 표시:

`zenity --question`

- "Hello!"라는 텍스트를 표시하는 정보 대화 상자 표시:

`zenity --info --text="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello!</span>`"`

- 이름/비밀번호 입력 폼을 표시하고 데이터를 ";"로 구분하여 출력:

`zenity --forms --add-entry="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`" --add-password="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>`" --separator="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`"`

- 사용자가 디렉토리만 선택할 수 있는 파일 선택 폼 표시:

`zenity --file-selection --directory`

- 매초 메시지를 업데이트하고 진행률을 보여주는 진행률 표시줄 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")</span>` | zenity --progress`
