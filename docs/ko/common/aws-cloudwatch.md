---
layout: page
title: common/aws-cloudwatch (한국어)
description: "AWS 리소스를 모니터링하여 리소스 이용률, 애플리케이션 성능 및 운영 상태에 대한 시스템 전반적인 가시성 확보."
content_hash: 9e68f4bbc931364047684f741dee213e288c3d3e
last_modified_at: 2023-10-01
related_topics:
  - title: English version
    url: /en/common/aws-cloudwatch.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws cloudwatch

AWS 리소스를 모니터링하여 리소스 이용률, 애플리케이션 성능 및 운영 상태에 대한 시스템 전반적인 가시성 확보.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html>.

- 대시보드 목록 나열:

`aws cloudwatch list-dashboards`

- 지정한 대시보드의 세부 정보 표시:

`aws cloudwatch get-dashboard --dashboard-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대시보드_이름</span>

- 메트릭 목록 나열:

`aws cloudwatch list-metrics`

- 알람(경보) 목록 나열:

`aws cloudwatch describe-alarms`

- 해당 매트릭과 연결된 알람 생성(또는 업데이트):

`aws cloudwatch put-metric-alarm --alarm-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알람_이름</span>` --evaluation-periods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">평가_주기</span>` --comparison-operator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비교_연산자</span>

- 지정한 알람들 삭제:

`aws cloudwatch delete-alarms --alarm_names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알람_이름</span>

- 지정한 대시보드들 삭제:

`aws cloudwatch delete-dashboards --dashboard-names `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대시보드_이름</span>
