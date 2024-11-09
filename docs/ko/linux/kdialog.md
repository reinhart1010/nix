---
layout: page
title: linux/kdialog (한국어)
description: "쉘 스크립트 내에서 KDE 대화 상자를 표시합니다."
content_hash: cc2d34deb3e54acaee1cfde6186b890f2139d4a8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/kdialog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/kdialog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdialog

쉘 스크립트 내에서 KDE 대화 상자를 표시합니다.
더 많은 정보: <https://develop.kde.org/docs/administration/kdialog/>.

- 특정 메시지를 표시하는 대화 상자 열기:

`kdialog --msgbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택_세부_메시지</span>`"`

- `예`와 `아니오` 버튼이 있는 질문 대화 상자를 열고, 각각 `0`과 `1`을 반환:

`kdialog --yesno "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- `예`, `아니오`, `취소` 버튼이 있는 경고 대화 상자를 열고, 각각 `0`, `1`, 또는 `2`를 반환:

`kdialog --warningyesnocancel "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 입력 대화 상자를 열고 `확인`을 누를 때 입력을 `stdout`에 출력:

`kdialog --inputbox "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택_기본_텍스트</span>`"`

- 특정 비밀번호를 요청하는 대화 상자를 열고 비밀번호를 `stdout`에 출력:

`kdialog --password "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 특정 드롭다운 메뉴가 포함된 대화 상자를 열고 선택한 항목을 `stdout`에 출력:

`kdialog --combobx "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목2</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>`"`

- 파일 선택 대화 상자를 열고 선택한 파일의 경로를 `stdout`에 출력:

`kdialog --getopenfilename`

- 진행 표시줄 대화 상자를 열고 통신을 위한 D-Bus 참조를 `stdout`에 출력:

`kdialog --progressbar "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`
