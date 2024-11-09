---
layout: page
title: common/terraform-output (한국어)
description: "Terraform 리소스에 대한 구조화된 데이터를 내보내기."
content_hash: f07750bdd89ac18dfdf08bc274ad71d039de26b3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/terraform-output.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/terraform-output.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/terraform-output.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># terraform output

Terraform 리소스에 대한 구조화된 데이터를 내보내기.
더 많은 정보: <https://developer.hashicorp.com/terraform/cli/commands/output>.

- 추가 인수 없이, `output`은 루트 모듈의 모든 출력을 표시:

`terraform output`

- 특정 이름의 값만 출력:

`terraform output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 출력 값을 일반 문자열로 변환 (쉘 스크립트에 유용):

`terraform output -raw`

- 출력을 각 출력별 키가 있는 JSON 객체로 포맷 (jq와 함께 사용 시 유용):

`terraform output -json`
