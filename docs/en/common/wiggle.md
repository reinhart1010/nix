---
layout: page
title: common/wiggle (English)
description: "A patch application tool resolving conflicts in patches that `patch` cannot handle."
content_hash: 3b91161c437b7878a40832a70b93938769a19780
last_modified_at: 2023-11-19
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wiggle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wiggle

A patch application tool resolving conflicts in patches that `patch` cannot handle.
Note: Wiggle forcefully applies all changes, merging when conflicts arise, and reporting unresolvable issues.
More information: <https://manned.org/wiggle>.

- Apply changes from the patch file to the original file:

`wiggle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_patch.patch</span>

- Apply changes to the [o]utput file:

`wiggle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_patch.patch</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>

- Take any changes in `file.rej` that could not have been applied and merge them into a file:

`wiggle --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.rej</span>

- E[x]tract one branch of a patch or merge file:

`wiggle -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_patch.patch</span>

- Apply a patch and save the compared words to the [o]utput file:

`wiggle --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/my_word_patch.patch</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/word_patched_code.c</span>

- Display help about the merge function:

`wiggle --merge --help`
