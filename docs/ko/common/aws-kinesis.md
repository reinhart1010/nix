---
layout: page
title: common/aws-kinesis (한국어)
description: "빅데이터를 스트리밍하는 실시간 처리를 위해 탄력적으로 확장되는 서비스인, Amazon Kinesis Data Streams와 상호작용함."
content_hash: fe8db7119be4032390caa56531cb92c8f7bf45f8
last_modified_at: 2024-09-24
related_topics:
  - title: Deutsch version
    url: /de/common/aws-kinesis.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-kinesis.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-kinesis.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-kinesis.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-kinesis.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-kinesis.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws kinesis

빅데이터를 스트리밍하는 실시간 처리를 위해 탄력적으로 확장되는 서비스인, Amazon Kinesis Data Streams와 상호작용함.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- 계정의 모든 스트림 표시:

`aws kinesis list-streams`

- Kinesis 스트림에 하나의 레코드 쓰기:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64로_인코딩된_메시지</span>

- 인라인 base64 인코딩을 사용하여 Kinesis 스트림에 레코드를 씀:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my raw message</span>`" | base64 )"`

- 스트림에서 사용 가능한 shard를 나열:

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 스트림의 shard에서 가장 오래된 메시지를 읽기 위한 shard 반복자를 가져옴:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>

- shard 반복자를 사용하여, shard에서 레코드를 읽음:

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">반복자</span>
