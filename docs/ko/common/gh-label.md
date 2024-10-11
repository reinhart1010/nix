---
layout: page
title: common/gh-label (한국어)
description: "GitHub 레이블 작업."
content_hash: 6c1e92f56700149cdc76f5e3a05b5ac9774f1a9d
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-label.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-label.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh label

GitHub 레이블 작업.
더 많은 정보: <https://cli.github.com/manual/gh_label>.

- 현재 디렉토리의 저장소에 대한 레이블 나열:

`gh label list`

- 현재 디렉토리의 저장소에 대한 레이블을 기본 웹 브라우저에서 보기:

`gh label list --web`

- 현재 디렉토리의 저장소에 특정 이름, 설명 및 16진수 형식 색상으로 레이블 생성:

`gh label create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`" --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색상_16진수</span>

- 현재 디렉토리의 저장소에 대한 레이블 삭제 (확인 요청):

`gh label delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 현재 디렉토리의 저장소에 특정 레이블의 이름과 설명 업데이트:

`gh label edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_이름</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설명</span>`"`

- 특정 저장소의 레이블을 현재 디렉토리의 저장소로 복제:

`gh label clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 하위 명령에 대한 도움말 표시:

`gh label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위_명령</span>` --help`
