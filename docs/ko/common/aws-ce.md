---
layout: page
title: common/aws-ce (한국어)
description: "AWS Cost Explorer 서비스를 통한 비용 관리 작업 수행합니다."
content_hash: 2c675074ecd9739f1d40c4a69a7ba5e18f00b902
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/aws-ce.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-ce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ce

AWS Cost Explorer 서비스를 통한 비용 관리 작업 수행합니다.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- 이상 모니터 생성:

`aws ce create-anomaly-monitor --monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모니터_이름</span>` --monitor-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모니터_유형</span>

- 이상 구독 생성:

`aws ce create-anomaly-subscription --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구독_이름</span>` --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모니터_arn</span>` --subscribers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구독자</span>

- 이상 조회:

`aws ce get-anomalies --monitor-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모니터_arn</span>` --start-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_날짜</span>` --end-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_날짜</span>

- 비용 및 사용량 조회:

`aws ce get-cost-and-usage --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_날짜</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_날짜</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세분화</span>` --metrics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메트릭</span>

- 비용 예측 조회:

`aws ce get-cost-forecast --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_날짜</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_날짜</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세분화</span>` --metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메트릭</span>

- 예약 사용량 조회:

`aws ce get-reservation-utilization --time-period `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작_날짜</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종료_날짜</span>` --granularity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세분화</span>

- 비용 카테고리 정의 목록 조회:

`aws ce list-cost-category-definitions`

- 리소스 태깅:

`aws ce tag-resource --resource-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>
