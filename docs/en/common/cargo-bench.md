---
layout: page
title: common/cargo-bench (English)
description: "Compile and execute benchmarks."
content_hash: 9958efc65642ba7c578de7bcab6cce65f1476fc3
last_modified_at: 2023-10-02
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo bench

Compile and execute benchmarks.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Execute all benchmarks of a package:

`cargo bench`

- Compile, but don’t run benchmarks:

`cargo bench --no-run`

- Benchmark only the specified packages:

`cargo bench --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Benchmark the specified benchmark:

`cargo bench --bench `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benchmark</span>

- Benchmark with the given profile (default: `bench`):

`cargo bench --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Benchmark all example targets:

`cargo bench --examples`

- Benchmark all binary targets:

`cargo bench --bins`

- Benchmark the package’s library:

`cargo bench --lib`
