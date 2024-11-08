---
layout: page
title: common/puppet-agent (한국어)
description: "Puppet 서버에서 클라이언트 구성을 가져와 로컬 호스트에 적용."
content_hash: ff6284f4f66eb6d22fd935476a13f45a23756bd9
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/puppet-agent.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/puppet-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# puppet agent

Puppet 서버에서 클라이언트 구성을 가져와 로컬 호스트에 적용.
더 많은 정보: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Puppet 서버에 노드를 등록하고 받은 카탈로그 적용:

`puppet agent --test --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puppetserver_fqdn</span>` --serverport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` --waitforcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poll_time</span>

- 에이전트를 백그라운드에서 실행 (`puppet.conf`의 설정 사용):

`puppet agent`

- 포그라운드에서 한 번 에이전트를 실행한 후 종료:

`puppet agent --test`

- 드라이 모드로 에이전트 실행:

`puppet agent --test --noop`

- 평가 중인 모든 리소스를 로그에 기록 (변경 사항이 없어도):

`puppet agent --test --evaltrace`

- 에이전트 비활성화:

`puppet agent --disable "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 에이전트 활성화:

`puppet agent --enable`
