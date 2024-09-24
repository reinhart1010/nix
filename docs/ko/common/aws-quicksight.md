---
layout: page
title: common/aws-quicksight (한국어)
description: "AWS QuickSight 엔터티를 생성, 삭제, 나열, 검색 및 업데이트."
content_hash: 5d597893005c80bc2fae95c3d11d4e3593f5e064
last_modified_at: 2024-09-24
related_topics:
  - title: Deutsch version
    url: /de/common/aws-quicksight.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-quicksight.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-quicksight.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-quicksight.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws quicksight

AWS QuickSight 엔터티를 생성, 삭제, 나열, 검색 및 업데이트.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- 데이터셋 나열:

`aws quicksight list-data-sets --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>

- 사용자 나열:

`aws quicksight list-users --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>` --namespace default`

- 그룹 나열:

`aws quicksight list-groups --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>` --namespace default`

- 대시보드 나열:

`aws quicksight list-dashboards --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>

- 데이터 세트에 대한 자세한 정보 표시:

`aws quicksight describe-data-set --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_셋_아이디</span>

- 데이터셋에 접근할 수 있는 사람과 해당 사용자가 데이터셋에서 수행할 수 있는 작업 종류를 표시:

`aws quicksight describe-data-set-permissions --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_계정_아이디</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_셋_아이디</span>
