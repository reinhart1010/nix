---
layout: page
title: linux/apx-stacks (한국어)
description: "`apx`에서 스택을 관리합니다."
content_hash: 82a8fb32082dc782bb6ddc4933616135585a67c9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/apx-stacks.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-stacks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apx-stacks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apx stacks

`apx`에서 스택을 관리합니다.
참고: 사용자가 생성한 스택 구성은 `~/.local/share/apx/stacks`에 저장됩니다.
더 많은 정보: <https://github.com/Vanilla-OS/apx>.

- 대화형으로 새로운 스택 구성 생성:

`apx stacks new`

- 대화형으로 스택 구성 업데이트:

`apx stacks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 사용 가능한 모든 스택 구성 나열:

`apx stacks list`

- 지정된 스택 구성 제거:

`apx stacks rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>

- 스택 구성 가져오기:

`apx stacks import --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/stack.yml</span>

- 스택 구성 내보내기 (참고: 출력 플래그는 선택 사항이며, 기본적으로 현재 작업 디렉터리에 내보내집니다):

`apx stacks export --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>
