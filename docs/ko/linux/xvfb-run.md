---
layout: page
title: linux/xvfb-run (한국어)
description: "가상 X 서버 환경에서 명령 실행."
content_hash: 20435066568b42dd0c7560b9b3b65cf34decedab
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/xvfb-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xvfb-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xvfb-run

가상 X 서버 환경에서 명령 실행.
더 많은 정보: <https://www.x.org/wiki/>.

- 가상 X 서버에서 지정된 명령 실행:

`xvfb-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 기본값(99)이 사용 불가능한 경우, 사용 가능한 서버 번호를 자동으로 선택:

`xvfb-run --auto-servernum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- Xvfb 서버에 인수 전달:

`xvfb-run --server-args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-screen 0 1024x768x24</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
