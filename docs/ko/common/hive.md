---
layout: page
title: common/hive (한국어)
description: "Apache Hive용 CLI 도구."
content_hash: d92c9c57e5af8e6dd52d33496e8268bb39dd1c10
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hive

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
