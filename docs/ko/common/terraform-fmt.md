---
layout: page
title: common/terraform-fmt (한국어)
description: "Terraform 언어 스타일 규칙에 따라 설정 파일을 포맷."
content_hash: 43f43a4819c889f3153f0021ff7caf923ebaeb26
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/terraform-fmt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/terraform-fmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/terraform-fmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># terraform fmt

Terraform 언어 스타일 규칙에 따라 설정 파일을 포맷.
더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/fmt>.

- 현재 디렉토리의 설정 파일을 포맷:

`terraform fmt`

- 현재 디렉토리 및 하위 디렉토리의 설정 파일을 포맷:

`terraform fmt -recursive`

- 포맷팅 변경 사항의 차이를 표시:

`terraform fmt -diff`

- 포맷된 파일을 `stdout`에 나열하지 않음:

`terraform fmt -list=false`
