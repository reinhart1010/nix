---
layout: page
title: common/aws-kinesis (English)
description: "Interact with the Amazon Kinesis Data Streams, a service that scales elastically for real-time processing of streaming big data."
content_hash: 00e6de1e23df5e001bddae309d90a68bbdb4e5f8
last_modified_at: 2024-03-04
related_topics:
  - title: Deutsch version
    url: /de/common/aws-kinesis.html
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
tldri18n_status: 2
---
# aws kinesis

Interact with the Amazon Kinesis Data Streams, a service that scales elastically for real-time processing of streaming big data.
More information: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Show all streams in the account:

`aws kinesis list-streams`

- Write one record to a Kinesis stream:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_encoded_message</span>

- Write a record to a Kinesis stream with inline base64 encoding:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my raw message</span>`" | base64 )"`

- List the shards available on a stream:

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Get a shard iterator for reading from the oldest message in a stream's shard:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Read records from a shard, using a shard iterator:

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iterator</span>
