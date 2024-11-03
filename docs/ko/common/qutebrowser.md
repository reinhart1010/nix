---
layout: page
title: common/qutebrowser (한국어)
description: "PyQt5 기반의 키보드 구동, vim 스타일 웹 브라우저."
content_hash: 0d8f9dea14e65aa3fb9a4b00750640a83d3daee2
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/qutebrowser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qutebrowser

PyQt5 기반의 키보드 구동, vim 스타일 웹 브라우저.
더 많은 정보: <https://qutebrowser.org/>.

- 지정된 저장소 디렉터리로 qutebrowser 열기:

`qutebrowser --basedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 임시 설정으로 qutebrowser 인스턴스 열기:

`qutebrowser --set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">content.geolocation</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>

- 지정된 이름의 세션을 복원하여 qutebrowser 인스턴스 열기:

`qutebrowser --restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>

- 지정된 방법으로 모든 URL을 열며 qutebrowser 실행:

`qutebrowser --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window</span>

- 임시 기본 디렉터리로 qutebrowser 열고 로그를 `stdout`에 JSON 형식으로 출력:

`qutebrowser --temp-basedir --json-logging`
