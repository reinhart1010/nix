---
layout: page
title: linux/qjoypad (한국어)
description: "게임패드나 조이스틱의 입력을 키보드 입력이나 마우스 동작으로 변환."
content_hash: f7cfc9d720bbd2b3825bcfd6c8f2e824b50e133a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/qjoypad.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/qjoypad.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qjoypad

게임패드나 조이스틱의 입력을 키보드 입력이나 마우스 동작으로 변환.
더 많은 정보: <https://qjoypad.sourceforge.net/>.

- QJoyPad 시작:

`qjoypad`

- QJoyPad를 시작하고 특정 디렉터리에서 장치를 검색:

`qjoypad --device=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- QJoyPad를 시작하지만 시스템 트레이 아이콘을 표시하지 않음:

`qjoypad --notray`

- QJoyPad를 시작하고 창 관리자가 시스템 트레이 아이콘을 사용하도록 강제:

`qjoypad --force-tray`

- 실행 중인 QJoyPad 인스턴스에 장치 및 레이아웃 목록 업데이트 강제:

`qjoypad --update`

- 이미 실행 중인 QJoyPad 인스턴스에 주어진 레이아웃을 로드하거나, 주어진 레이아웃을 사용하여 QJoyPad 시작:

`qjoypad "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이아웃</span>`"`
