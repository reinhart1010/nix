---
layout: page
title: common/mysql_secure_installation (한국어)
description: "MySQL을 보다 안전하게 설정."
content_hash: e90c14f657506faf91d1dfb4e57f7f2902f17cf0
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/mysql_secure_installation.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mysql_secure_installation.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mysql_secure_installation

MySQL을 보다 안전하게 설정.
더 많은 정보: <https://dev.mysql.com/doc/refman/en/mysql-secure-installation.html>.

- 대화형 설정 시작:

`mysql_secure_installation`

- 특정 호스트와 포트 사용:

`mysql_secure_installation --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 도움말 표시:

`mysql_secure_installation --help`
