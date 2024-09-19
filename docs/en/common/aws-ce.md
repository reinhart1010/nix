---
layout: page
title: common/aws-ce (English)
description: "Run cost management operations through the AWS Cost Explorer service."
content_hash: 36cd514b55dc1db287725daa5aeff7fe4d5e287f
last_modified_at: 2024-09-19
related_topics:
  - title: español version
    url: /es/common/aws-ce.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-ce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ce

Run cost management operations through the AWS Cost Explorer service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- Create anomaly monitor:

`aws ce create-anomaly-monitor --monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_name</span>` --monitor-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_type</span>

- Create anomaly subscription:

`aws ce create-anomaly-subscription --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_name</span>` --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_arn</span>` --subscribers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscribers</span>

- Get anomalies:

`aws ce get-anomalies --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_arn</span>` --start-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_time</span>` --end-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_time</span>

- Get cost and usage:

`aws ce get-cost-and-usage --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularity</span>` --metrics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metrics</span>

- Get cost forecast:

`aws ce get-cost-forecast --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularity</span>` --metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>

- Get reservation utilization:

`aws ce get-reservation-utilization --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">granularity</span>

- List cost category definitions:

`aws ce list-cost-category-definitions`

- Tag resource:

`aws ce tag-resource --resource-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tags</span>
