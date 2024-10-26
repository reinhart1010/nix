---
layout: page
title: common/az-login (中文 (繁體, 台灣))
description: "登入到 Azure。"
content_hash: b1d22467040aee0f065b7e39efc86c5cc7613024
last_modified_at: 2024-10-26
related_topics:
  - title: Deutsch version
    url: /de/common/az-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/az-login.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/az-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az login

登入到 Azure。
`azure-cli` 的一部分（也稱為 `az`）。
更多資訊：<https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- 以互動方式進行登入：

`az login`

- 使用客戶端密鑰登入服務主體：

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- 使用客戶端憑證登入服務主體：

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路徑/到/憑證.pem</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- 使用 VM 的系統指派身份登入：

`az login --identity`

- 使用 VM 的使用者分配身份登入：

`az login --identity --username /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subscription_id</span>`/resourcegroups/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_rg</span>`/providers/Microsoft.ManagedIdentity/userAssignedIdentities/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_id</span>
