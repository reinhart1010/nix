---
layout: page
title: common/influx (한국어)
description: "InfluxDB 커멘드 라인 클라이언트."
content_hash: 3ccd4fb4a130a66c69f2f5250dab2bdadb10374e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/influx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# influx

InfluxDB 커멘드 라인 클라이언트.
더 많은 정보: <https://docs.influxdata.com/influxdb/v1.7/tools/shell/>.

- 자격증명 없이 localhost에서 실행되는 InfluxDB에 연결:

`influx`

- 특정 사용자 이름으로 연결 (비밀번호를 묻는 메시지가 표시됨):

`influx -username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -password ""`

- 특정 호스트에 연결:

`influx -host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 특정 데이터베이스 사용:

`influx -database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>

- 주어진 명령을 실행:

`influx -execute "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">influxql_명령</span>`"`

- 특정 형식으로 출력을 반환:

`influx -execute "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">influxql_명령</span>`" -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|csv|column</span>
