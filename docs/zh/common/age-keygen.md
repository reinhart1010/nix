---
layout: page
title: common/age-keygen (中文)
description: "生成 `age` 密钥对。"
content_hash: 3cbd0a61e286cc48ecea951be76fe52243fc3925
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/common/age-keygen.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/age-keygen.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age-keygen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age-keygen

生成 `age` 密钥对。
参见：`age` 用于加密/解密文件。
更多信息：<https://manned.org/age-keygen>.

- 生成密钥对，将其保存到未加密文件，并将公钥打印到标准输出：

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将身份转换为接收者，并将公钥打印到标准输出：

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
