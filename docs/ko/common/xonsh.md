---
layout: page
title: common/xonsh (한국어)
description: "Python 기반의 크로스 플랫폼 및 Unix 지향 셸."
content_hash: 955384b958849b0a27d4f304346d711a458d22f2
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xonsh.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xonsh.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xonsh

Python 기반의 크로스 플랫폼 및 Unix 지향 셸.
Xonsh(발음: conch)에서 sh/Python 코드를 작성하고 혼합할 수 있습니다.
더 많은 정보: <https://xon.sh>.

- 대화형 셸 세션 시작:

`xonsh`

- 단일 명령 실행 후 종료:

`xonsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- 스크립트 파일에서 명령을 실행하고 종료:

`xonsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트_파일.xonsh</span>

- 셸 프로세스를 위한 환경 변수를 정의:

`xonsh -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값1</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값2</span>

- 지정된 `.xonsh` 또는 `.json` 설정 파일 로드:

`xonsh --rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.xonsh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.json</span>

- `.xonshrc` 설정 파일 로딩 건너뜀:

`xonsh --no-rc`
