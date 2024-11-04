---
layout: page
title: common/velero (한국어)
description: "Kubernetes 애플리케이션 및 그들의 지속 볼륨을 백업 및 마이그레이션."
content_hash: c4eea29597dd8c78f82d920ecf0be7a67cfc95cc
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/velero.html
    icon: bi bi-globe
tldri18n_status: 2
---
# velero

Kubernetes 애플리케이션 및 그들의 지속 볼륨을 백업 및 마이그레이션.
더 많은 정보: <https://github.com/heptio/velero>.

- 모든 리소스를 포함하는 백업 생성:

`velero backup create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업_이름</span>

- 모든 백업 나열:

`velero backup get`

- 백업 삭제:

`velero backup delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업_이름</span>

- 주간 백업 생성, 각각 90일(2160시간) 동안 유지:

`velero schedule create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스케줄_이름</span>` --schedules="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@every 7d</span>`" --ttl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2160h0m0s</span>

- 특정 스케줄에 의해 트리거된 최신 성공적인 백업에서 복원 생성:

`velero restore create --from-schedule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스케줄_이름</span>
