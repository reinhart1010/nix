---
layout: page
title: common/pamenlarge (English)
description: "Enlarge a PAM image by duplicating pixels."
content_hash: d5d5a8ac4def270ec74087d5f86af86a8e63c1a1
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pamenlarge

Enlarge a PAM image by duplicating pixels.
See also: `pbmreduce`, `pamditherbw`, `pbmpscale`.
More information: <https://netpbm.sourceforge.net/doc/pamenlarge.html>.

- Enlarge the specified image by the specified factor:

`pamenlarge -scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Enlarge the specified image by the specified factors horizontally and vertically:

`pamenlarge -xscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">XN</span>` -yscale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
