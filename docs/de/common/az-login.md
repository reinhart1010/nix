---
layout: page
title: common/az-login (Deutsch)
description: "Melden Sie sich bei Azure an."
content_hash: 2066ba4ace665beee042ea523b5a483d24604799
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/az-login.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/az-login.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/az-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az login

Melden Sie sich bei Azure an.
Teil von `azure-cli` (auch bekannt als `az`).
Weitere Informationen: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Melden Sie sich interaktiv an:

`az login`

- Melden Sie sich mit einem Dienstprinzipal mit dem geheimen Clientschlüssel an:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Melden Sie sich mit einem Dienstprinzipal mithilfe des Clientzertifikats an:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Melden Sie sich mit der vom System zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity`

- Melden Sie sich mit der vom Benutzer zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity --username /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>`/resourcegroups/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_rg</span>`/providers/Microsoft.ManagedIdentity/userAssignedIdentities/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_id</span>
