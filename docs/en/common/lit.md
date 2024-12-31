---
layout: page
title: common/lit (English)
description: "LLVM integrated tester for executing LLVM and Clang style test suites, summarizing results."
content_hash: 2a7f0ab91ff8cc48adf6fb9d65bfe6e21a7ccc1c
last_modified_at: 2024-12-31
tldri18n_status: 2
---
# lit

LLVM integrated tester for executing LLVM and Clang style test suites, summarizing results.
Part of LLVM.
More information: <https://www.llvm.org/docs/CommandGuide/lit.html>.

- Run a specified test case:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test_file.test</span>

- Run all test cases in a specified directory:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test_suite</span>

- Run all test cases and check the wall time for each cases, then report to summary output:

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test_suite</span>` --time-tests`

- Run individual tests with Valgrind (memory check and memory leak test):

`lit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test_file.test</span>` --vg --vg-leak --vg-args=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">args_to_valgrind</span>
