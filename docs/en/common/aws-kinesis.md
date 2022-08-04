---
layout: page
title: common/aws-kinesis (English)
description: "Official AWS CLI for Amazon Kinesis streaming data services."
content_hash: b6d6bc45c448e176b51cbd3d35d848757d3980b1
related_topics:
  - title: Deutsch version
    url: /de/common/aws-kinesis.html
    icon: bi bi-globe
---
# aws kinesis

Official AWS CLI for Amazon Kinesis streaming data services.
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
