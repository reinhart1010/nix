---
layout: page
title: common/aws-kinesis (Deutsch)
description: "Offizielles AWS CLI für die Amazon Kinesis-Streaming-Datenplattform."
content_hash: 9aa977e8894da2fbe94416b19923a7a28fd0a734
related_topics:
  - title: English version
    url: /en/common/aws-kinesis.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-kinesis.html
    icon: bi bi-globe
---
# aws kinesis

Offizielles AWS CLI für die Amazon Kinesis-Streaming-Datenplattform.
Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html#cli-aws-kinesis>.

- Liste alle Streams auf:

`aws kinesis list-streams`

- Schreibe einen Datensatz in einen Kinesis Stream:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüssel</span>` --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64_codierte_nachricht</span>

- Schreibe einen Datensatz in einen Kinesis Stream mit base64 inline Encodierung:

`aws kinesis put-record --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --partition-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüssel</span>` --data "$( echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meine nachricht</span>`" | base64 )"`

- Liste alle verfügbaren Shards in einem Stream auf:

`aws kinesis list-shards --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Rufe einen Shard Iterators auf, um diesen beginnend mit der ältesten Nachricht auszulesen:

`aws kinesis get-shard-iterator --shard-iterator-type TRIM_HORIZON --stream-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --shard-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Lies einen Datensatz aus einem Shard über einen Shard Iterator:

`aws kinesis get-records --shard-iterator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iterator</span>
