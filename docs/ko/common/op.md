---
layout: page
title: common/op (한국어)
description: "1Password의 데스크탑 앱을 위한 공식 CLI."
content_hash: ddafc6222dea8687aa549f4b3f0266bb22a2125d
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/op.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/op.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># op

1Password의 데스크탑 앱을 위한 공식 CLI.
더 많은 정보: <https://developer.1password.com/docs/cli/reference>.

- 1Password 계정에 로그인:

`op signin`

- 모든 금고 나열:

`op vault list`

- 항목 세부 정보를 JSON 형식으로 출력:

`op item get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_이름</span>` --format json`

- 기본 금고에 카테고리를 지정하여 새 항목 생성:

`op item create --category `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">카테고리_이름</span>

- 참조된 비밀을 `stdout`에 출력:

`op read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_참조</span>

- 내보낸 환경 변수에서 비밀 참조를 명령에 전달:

`op run -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 환경 파일에서 비밀 참조를 명령에 전달:

`op run --env-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/환경_파일.env</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 파일에서 비밀 참조를 읽어 일반 텍스트 비밀을 파일에 저장:

`op inject --in-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>
