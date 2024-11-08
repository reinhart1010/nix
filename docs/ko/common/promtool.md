---
layout: page
title: common/promtool (한국어)
description: "Prometheus 모니터링 시스템을 위한 도구."
content_hash: 46705c095dee2f74befe2a5f31bff3e96987ada1
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/promtool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# promtool

Prometheus 모니터링 시스템을 위한 도구.
더 많은 정보: <https://prometheus.io/docs/prometheus/latest/getting_started/>.

- 구성 파일이 유효한지 여부 확인 (오류가 있을 경우 보고):

`promtool check config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_파일.yml</span>

- 규칙 파일이 유효한지 여부 확인 (오류가 있을 경우 보고):

`promtool check rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_파일.yml</span>

- `stdin`을 통해 Prometheus 메트릭을 전달하여 일관성과 정확성을 확인:

`curl --silent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com:9090/metrics/</span>` | promtool check metrics`

- 규칙 구성에 대한 단위 테스트:

`promtool test rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트_파일.yml</span>
