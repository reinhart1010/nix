---
layout: page
title: common/pulumi-stack (한국어)
description: "스택을 관리하고 스택 상태를 확인."
content_hash: 4e95c9a7b6b144b58e0f8677b1738667145f54ae
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pulumi-stack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-stack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi stack

스택을 관리하고 스택 상태를 확인.
더 많은 정보: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- 새 스택 생성:

`pulumi stack init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름</span>

- 스택 상태 보기:

`pulumi stack`

- 현재 프로젝트의 스택 나열:

`pulumi stack ls`

- 모든 프로젝트의 스택 나열:

`pulumi stack ls --all`

- 활성 스택 선택:

`pulumi stack select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름</span>

- 스택 출력을 평문으로 표시 (비밀 포함):

`pulumi stack output --show-secrets`

- 스택 상태를 JSON 파일로 내보내기:

`pulumi stack export --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- 도움말 표시:

`pulumi stack --help`
