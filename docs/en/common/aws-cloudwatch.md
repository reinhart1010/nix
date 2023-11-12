---
layout: page
title: common/aws-cloudwatch (English)
description: "Monitor AWS resources to gain system-wide visibility into resource utilization, application performance, and operational health."
content_hash: a2bc5183fc0665434afcd916362e577151bf1878
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/aws-cloudwatch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cloudwatch

Monitor AWS resources to gain system-wide visibility into resource utilization, application performance, and operational health.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html>.

- List dashboards for your account:

`aws cloudwatch list-dashboards`

- Display details for the specified dashboard:

`aws cloudwatch get-dashboard --dashboard-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dashboard_name</span>

- List metrics:

`aws cloudwatch list-metrics`

- List alarms:

`aws cloudwatch describe-alarms`

- Create or update an alarm and associate it with a metric:

`aws cloudwatch put-metric-alarm --alarm-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alarm_name</span>` --evaluation-periods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">evaluation_periods</span>` --comparison-operator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comparison_operator</span>

- Delete the specified alarms:

`aws cloudwatch delete-alarms --alarm_names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alarm_names</span>

- Delete the specified dashboards:

`aws cloudwatch delete-dashboards --dashboard-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dashboard_names</span>
