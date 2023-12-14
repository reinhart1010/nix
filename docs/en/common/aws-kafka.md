---
layout: page
title: common/aws-kafka (English)
description: "Manage an Amazon MSK (Managed Streaming for Apache Kafka) cluster."
content_hash: 001155c2a4ea68fcdf5a9b42966d7d209669cc94
last_modified_at: 2023-12-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-kafka.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws kafka

Manage an Amazon MSK (Managed Streaming for Apache Kafka) cluster.
See also: `aws`.
More information: <https://docs.aws.amazon.com/cli/latest/reference/kafka/index.html>.

- Create a new MSK cluster:

`aws kafka create-cluster --cluster-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_name</span>` --broker-node-group-info instanceType=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instance_type</span>`,clientSubnets=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet_id1 subnet_id2 ...</span>` --kafka-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>` --number-of-broker-nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number</span>

- Describe a MSK cluster:

`aws kafka describe-cluster --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>

- List all MSK clusters in the current region:

`aws kafka list-clusters`

- Create a new MSK configuration:

`aws kafka create-configuration --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_name</span>` --server-properties file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration_file.txt</span>

- Describe a MSK configuration:

`aws kafka describe-configuration --arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_arn</span>

- List all MSK configurations in the current region:

`aws kafka list-configurations`

- Update the MSK cluster configuration:

`aws kafka update-cluster-configuration --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>` --configuration-info arn=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_arn</span>`,revision=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuration_revision</span>

- Delete the MSK cluster:

`aws kafka delete-cluster --cluster-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster_arn</span>
