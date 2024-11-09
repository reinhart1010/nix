---
layout: page
title: common/terragrunt (한국어)
description: "Terraform CLI 인수를 DRY하게 유지."
content_hash: 916b4234aac50f54fcd060ad7bb87eee70f7a4bf
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/terragrunt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/terragrunt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># terragrunt

Terraform CLI 인수를 DRY하게 유지.
더 많은 정보: <https://terragrunt.gruntwork.io>.

- 실행 계획 생성 및 표시:

`terragrunt plan`

- 인프라 생성 또는 변경:

`terragrunt apply`

- 현재 배포 상태 표시:

`terragrunt show`

- 모듈 출력 값 표시:

`terragrunt output`

- Terraform이 관리하는 인프라 파괴:

`terragrunt destroy`

- Terragrunt 모듈 트리(스택)에서 인프라 생성 또는 변경:

`terragrunt run-all apply`
