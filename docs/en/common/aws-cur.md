---
layout: page
title: common/aws-cur (English)
description: "Create, query, and delete AWS usage report definitions."
content_hash: d2727c6a8497518874ab1869256623b2bc6d5615
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/aws-cur.html
    icon: bi bi-globe
---
# aws cur

Create, query, and delete AWS usage report definitions.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Create an AWS cost and usage report definition from a JSON file:

`aws cur put-report-definition --report-definition file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report_definition.json</span>

- List usage report definitions defined for the logged in account:

`aws cur describe-report-definitions`

- Delete a usage report definition:

`aws cur --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_region</span>` delete-report-definition --report-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>
