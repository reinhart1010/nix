---
layout: page
title: common/terraform (한국어)
description: "코드로 인프라를 생성하고 클라우드 제공업체에 배포."
content_hash: 93a9c1e79e9a371349dfcbac64f67ce59b930de9
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/terraform.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/terraform.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/terraform.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># terraform

코드로 인프라를 생성하고 클라우드 제공업체에 배포.
더 많은 정보: <https://www.terraform.io/>.

- 새 또는 기존 Terraform 구성 초기화:

`terraform init`

- 구성 파일의 구문이 올바른지 확인:

`terraform validate`

- Terraform 언어 스타일 규칙에 따라 구성 포맷팅:

`terraform fmt`

- 실행 계획 생성 및 표시:

`terraform plan`

- 인프라 생성 또는 변경:

`terraform apply`

- Terraform에서 관리하는 인프라 파괴:

`terraform destroy`
