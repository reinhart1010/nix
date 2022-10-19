---
layout: page
title: common/az-login (Deutsch)
description: "Melden Sie sich bei Azure an."
content_hash: 479688323d5baad1f1167437a91e60989f3ceb7f
related_topics:
  - title: English version
    url: /en/common/az-login.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az login

Melden Sie sich bei Azure an.
Teil von `az`, der Befehlszeilenschnittstelle von Azure.
Weitere Informationen: <https://learn.microsoft.com/cli/azure/reference-index#az_login>.

- Melden Sie sich interaktiv an:

`az login`

- Melden Sie sich mit einem Dienstprinzipal mit dem geheimen Clientschlüssel an:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --passsword `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Melden Sie sich mit einem Dienstprinzipal mithilfe des Clientzertifikats an:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/cert.pem</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- Melden Sie sich mit der vom System zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity`

- Melden Sie sich mit der vom Benutzer zugewiesenen verwalteten Identität eines virtuellen Computers an:

`az login --identity --username /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>`/resourcegroups/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_rg</span>`/providers/Microsoft.ManagedIdentity/userAssignedIdentities/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_id</span>
