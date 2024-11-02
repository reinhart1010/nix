---
layout: page
title: common/watchexec (한국어)
description: "파일이 변경될 때 임의의 명령을 실행."
content_hash: 114b5e0412856ac5147ffd91e9c9644e653bd10b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/watchexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/watchexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># watchexec

파일이 변경될 때 임의의 명령을 실행.
더 많은 정보: <https://github.com/watchexec/watchexec>.

- 현재 디렉토리의 파일이 변경될 때 `ls -la` 실행:

`watchexec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -la</span>

- 현재 디렉토리의 JavaScript, CSS, HTML 파일이 변경될 때 `make` 실행:

`watchexec --exts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">js,css,html</span>` make`

- `lib` 또는 `src` 디렉토리의 파일이 변경될 때 `make` 실행:

`watchexec --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lib</span>` --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- 현재 디렉토리의 파일이 변경될 때 `my_server` 호출/재시작, 자식 프로세스를 중지하기 위해 `SIGKILL` 신호 전송:

`watchexec --restart --stop-signal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGKILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_server</span>
