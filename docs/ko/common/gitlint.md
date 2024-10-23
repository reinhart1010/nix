---
layout: page
title: common/gitlint (한국어)
description: "Git 커밋 메시지 린터는 커밋 메시지의 스타일을 확인."
content_hash: b80611f3a20b8fddeb7de684082eafe31bb67235
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitlint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitlint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitlint

Git 커밋 메시지 린터는 커밋 메시지의 스타일을 확인.
더 많은 정보: <https://jorisroovers.com/gitlint/>.

- 마지막 커밋 메시지를 확인:

`gitlint`

- 린트에 대한 커밋 범위:

`gitlint --commits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단일_refspec_인수</span>

- 추가 사용자 정의 규칙이 있는 디렉토리 또는 Python 모듈의 경로 표시:

`gitlint --extra-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 특정 CI 작업 시작:

`gitlint --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>

- commit-msg가 포함된 파일의 경로 표시:

`gitlint --msg-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일이름</span>

- 로컬 저장소에서 단계적 커밋 메타 정보를 읽음:

`gitlint --staged`
