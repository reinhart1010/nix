---
layout: page
title: common/odps (한국어)
description: "Aliyun ODPS (Open Data Processing Service) 명령줄 도구."
content_hash: 42f23a602388bb52bba1e89d202cc2ca9fa31fed
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/odps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/odps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># odps

Aliyun ODPS (Open Data Processing Service) 명령줄 도구.
`inst`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://www.alibabacloud.com/help/doc-detail/27971.htm>.

- 사용자 지정 구성 파일로 명령줄 시작:

`odpscmd --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">odps_config.ini</span>

- 현재 프로젝트 변경:

`use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>`;`

- 현재 프로젝트의 테이블 표시:

`show tables;`

- 테이블 설명:

`desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`;`

- 테이블 파티션 표시:

`show partitions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>`;`

- 파티션 설명:

`desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테이블_이름</span>` partition (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_명세</span>`);`
