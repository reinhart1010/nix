---
layout: page
title: common/valgrind (English)
description: "Wrapper for a set of expert tools for profiling, optimizing and debugging programs."
content_hash: 258a354fc8b76b7649d4d0d3fae81d8757401ff2
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# valgrind

Wrapper for a set of expert tools for profiling, optimizing and debugging programs.
Commonly used tools include `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind`, and `drd`.
More information: <https://www.valgrind.org>.

- Use the (default) Memcheck tool to show a diagnostic of memory usage by `program`:

`valgrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Use Memcheck to report all possible memory leaks of `program` in full detail:

`valgrind --leak-check=full --show-leak-kinds=all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Use the Cachegrind tool to profile and log CPU cache operations of `program`:

`valgrind --tool=cachegrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Use the Massif tool to profile and log heap memory and stack usage of `program`:

`valgrind --tool=massif --stacks=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
