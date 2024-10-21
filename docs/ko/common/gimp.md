---
layout: page
title: common/gimp (한국어)
description: "GNU 이미지 조작 프로그램."
content_hash: 8f8fc111c556e5418086c590dec4eb84e2bcfe7d
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gimp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gimp.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/gimp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gimp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gimp

GNU 이미지 조작 프로그램.
참고: `krita`.
더 많은 정보: <https://docs.gimp.org/en/gimp-fire-up.html#gimp-concepts-running-command-line>.

- GIMP 시작:

`gimp`

- 특정 파일 열기:

`gimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2 ...</span>

- 새로운 창에서 특정 파일 열기:

`gimp --new-instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1 경로/대상/이미지2 ...</span>

- 스플래시 화면 없이 시작:

`gimp --no-splash`

- 오류 및 경고를 대화 상자에 표시하는 대신 콘솔에 출력:

`gimp --console-messages`

- 디버깅 신호 처리기 활성화:

`gimp --debug-handlers`
