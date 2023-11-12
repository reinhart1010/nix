---
layout: page
title: linux/restorecon (English)
description: "Restore SELinux security context on files/directories according to persistent rules."
content_hash: b7f1b8fe378b3d035ec69009fee960276d854b22
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# restorecon

Restore SELinux security context on files/directories according to persistent rules.
See also: `semanage-fcontext`.
More information: <https://manned.org/restorecon>.

- View the current security context of a file or directory:

`ls -dlZ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Restore the security context of a file or directory:

`restorecon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Restore the security context of a directory recursively, and show all changed labels:

`restorecon -R -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Restore the security context of a directory recursively, using all available threads, and show progress:

`restorecon -R -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Preview the label changes that would happen without applying them:

`restorecon -R -n -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
