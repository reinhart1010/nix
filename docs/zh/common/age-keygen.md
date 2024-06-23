---
layout: page
title: common/age-keygen (中文)
description: "生成 `age` 密钥对。"
content_hash: 9532339c303da550ed15e3b5ec3564575d552193
last_modified_at: 2024-06-23
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/age-keygen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># age-keygen

生成 `age` 密钥对。
参见：`age` 用于加密/解密文件。
更多信息： <https://manned.org/age-keygen>.

- 生成密钥对，将其保存到未加密文件，并将公钥打印到标准输出：

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将身份转换为接收者，并将公钥打印到标准输出：

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
