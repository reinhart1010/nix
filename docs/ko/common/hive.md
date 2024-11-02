---
layout: page
title: common/hive (한국어)
description: "Apache Hive용 CLI 도구."
content_hash: d92c9c57e5af8e6dd52d33496e8268bb39dd1c10
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/hive.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hive.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hive

Apache Hive용 CLI 도구.
더 많은 정보: <https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Cli>.

- Hive 대화형 쉘을 시작:

`hive`

- HiveQL 실행:

`hive -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hiveql_쿼리</span>`"`

- 변수 대체를 사용해서 HiveQL 파일을 실행:

`hive --define `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sql</span>

- HiveConfig를 사용해 HiveQL을 실행 (예: `mapred.reduce.tasks=32`):

`hive --hiveconf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_값</span>
