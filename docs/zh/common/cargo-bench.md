---
layout: page
title: common/cargo-bench (中文)
description: "编译并执行基准测试。"
content_hash: 453466cafcf6f585af93ca80070af8d722ba259c
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-bench.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-bench.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo bench

编译并执行基准测试。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- 执行包的所有基准测试：

`cargo bench`

- 在基准测试失败时不停止：

`cargo bench --no-fail-fast`

- 编译，但不运行基准测试：

`cargo bench --no-run`

- 对指定的基准进行基准测试：

`cargo bench --bench `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">基准测试名称</span>

- 使用给定的配置文件进行基准测试 (默认为 `bench`)：

`cargo bench --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件</span>

- 对所有示例目标进行基准测试：

`cargo bench --examples`

- 对所有二进制目标进行基准测试：

`cargo bench --bins`

- 对包的库(lib)进行基准测试：

`cargo bench --lib`
