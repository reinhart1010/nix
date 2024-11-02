---
layout: page
title: common/py-spy (한국어)
description: "Python 프로그램용 샘플링 프로파일러."
content_hash: 5395600e378ad1fa02fa71875c05d2bed22f25c8
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/py-spy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/py-spy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># py-spy

Python 프로그램용 샘플링 프로파일러.
더 많은 정보: <https://github.com/benfred/py-spy>.

- 실행 중인 프로세스에서 가장 많은 실행 시간을 차지하는 함수의 실시간 보기 표시:

`py-spy top --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 프로그램을 시작하고 가장 많은 실행 시간을 차지하는 함수의 실시간 보기 표시:

`py-spy top -- python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 함수 호출 실행 시간의 SVG 플레임 그래프 생성:

`py-spy record -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로필.svg</span>` --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 실행 중인 프로세스의 호출 스택 덤프:

`py-spy dump --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
