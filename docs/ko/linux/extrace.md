---
layout: page
title: linux/extrace (한국어)
description: "exec() 호출을 추적합니다."
content_hash: 09d29282f6e4d964ee16df5a22bf4668619cad10
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/extrace.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/extrace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># extrace

exec() 호출을 추적합니다.
더 많은 정보: <https://github.com/chneukirchen/extrace>.

- 시스템에서 발생하는 모든 프로그램 실행을 추적:

`sudo extrace`

- 명령을 실행하고 해당 명령의 하위 프로세스만 추적:

`sudo extrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 각 프로세스의 현재 작업 디렉터리 출력:

`sudo extrace -d`

- 각 실행 파일의 전체 경로 해석:

`sudo extrace -l`

- 각 프로세스를 실행하는 사용자 표시:

`sudo extrace -u`
