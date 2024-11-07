---
layout: page
title: common/pulumi-up (한국어)
description: "스택의 리소스를 생성하거나 업데이트."
content_hash: 6a1830c4d0db8850e61c1a2574fef649c9e6b5fe
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pulumi-up.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-up.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi up

스택의 리소스를 생성하거나 업데이트.
더 많은 정보: <https://www.pulumi.com/docs/cli/commands/pulumi_up/>.

- 프로그램 및/또는 인프라에 대한 변경 사항 미리보기 및 배포:

`pulumi up`

- 미리보기 후 자동 승인 및 업데이트 수행:

`pulumi up --yes`

- 특정 스택에서 변경 사항 미리보기 및 배포:

`pulumi up --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택</span>

- 스택 출력을 표시하지 않음:

`pulumi up --suppress-outputs`

- 오류가 발생하더라도 리소스 업데이트 계속 진행:

`pulumi up --continue-on-error`
