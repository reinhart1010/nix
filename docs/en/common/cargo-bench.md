---
layout: page
title: common/cargo-bench (English)
description: "Compile and execute benchmarks."
content_hash: ae536d896a91c5a43c6b9ded84f7edb5ce8df0e6
last_modified_at: 2023-10-30
---
# cargo bench

Compile and execute benchmarks.
More information: <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Execute all benchmarks of a package:

`cargo bench`

- Don't stop when a benchmark fails:

`cargo bench --no-fail-fast`

- Compile, but don’t run benchmarks:

`cargo bench --no-run`

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
