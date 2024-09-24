---
layout: page
title: common/aws-rds (한국어)
description: "관계형 데이터베이스를 설정, 운영 및 확장하기 위한 웹 서비스인 AWS Relational Database Service를 사용."
content_hash: 7beaa791303d1265576ac36490b14cd27fb81db3
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/aws-rds.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-rds.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-rds.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-rds.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws rds

관계형 데이터베이스를 설정, 운영 및 확장하기 위한 웹 서비스인 AWS Relational Database Service를 사용.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- 특정 RDS 하위 명령어에 대한 도움말을 표시:

`aws rds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>` help`

- 인스턴스 중지:

`aws rds stop-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_구분자</span>

- 인스턴스 시작:

`aws rds start-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_구분자</span>

- RDS 인스턴스 수정:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">매개변수</span>` --apply-immediately`

- RDS 인스턴스에 업데이트 적용:

`aws rds apply-pending-maintenance-action --resource-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_arn</span>` --apply-action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system-update</span>` --opt-in-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immediate</span>

- 인스턴스 구분자 변경:

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오래된_인스턴스_구분자</span>` --new-db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_인스턴스_구분자</span>

- 인스턴스 재부팅:

`aws rds reboot-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_구분자</span>

- 인스턴스 삭제:

`aws rds delete-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인스턴스_구분자</span>` --final-db-snapshot-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_구분자</span>` --delete-automated-backups`
