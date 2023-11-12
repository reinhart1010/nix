---
layout: page
title: common/semver (English)
description: "Semantic version string parser."
content_hash: a847469cd89e1926968294b04d83569a244f6d19
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# semver

Semantic version string parser.
More information: <https://github.com/npm/node-semver>.

- Check if a version string respects the semantic versioning format (prints an empty string if it does not match):

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>

- Convert a version string to the semantic versioning format:

`semver --coerce `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>

- Test if `1.2.3` matches the `^1.0` range (prints an empty string if it does not match):

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` --range "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^1.0</span>`"`

- Test with multiple ranges:

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">">=1.0"</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"<2.0"</span>

- Test multiple version strings and return only the ones that match:

`semver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0.0</span>` --range "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^1.0</span>`"`
