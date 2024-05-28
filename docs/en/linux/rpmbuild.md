---
layout: page
title: linux/rpmbuild (English)
description: "RPM Package Build tool."
content_hash: cc357eadfad90792de2e6b8f3a2f3d6648df757f
last_modified_at: 2024-05-28
tldri18n_status: 2
---
# rpmbuild

RPM Package Build tool.
More information: <https://manned.org/man/rpmbuild>.

- Build binary and source packages:

`rpmbuild -ba `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/spec_file</span>

- Build a binary package without source package:

`rpmbuild -bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/spec_file</span>

- Specify additional variables when building a package:

`rpmbuild -bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/spec_file</span>` --define "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value1</span>`" --define "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value2</span>`"`
