---
layout: page
title: common/aws-iam (한국어)
description: "AWS 서비스에 대한 접근을 안전하게 제어하기 위한 웹 서비스인 IAM(Identity and Access Management)과 상호작용."
content_hash: 2281160a5601e341753b9605811bfceaaa919130
last_modified_at: 2024-09-21
related_topics:
  - title: Deutsch version
    url: /de/common/aws-iam.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-iam.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-iam.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-iam.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-iam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws iam

AWS 서비스에 대한 접근을 안전하게 제어하기 위한 웹 서비스인 IAM(Identity and Access Management)과 상호작용.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- 사용자 나열:

`aws iam list-users`

- 정책 나열:

`aws iam list-policies`

- 그룹 나열:

`aws iam list-groups`

- 그룹 내 사용자 가져오기:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- IAM 정책 표시:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_이름</span>

- 액세스 키 나열:

`aws iam list-access-keys`

- 특정 사용자의 액세스 키 나열:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>

- 도움말 표시:

`aws iam help`
