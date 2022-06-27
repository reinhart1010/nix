---
layout: page
title: common/bash-it (English)
description: "A collection of community contributed Bash commands and scripts for Bash 3.2+."
content_hash: bc39e5269cdb23613f5c85a62e1b4e684d4c0cfd
---
# bash-it

A collection of community contributed Bash commands and scripts for Bash 3.2+.
More information: <https://bash-it.readthedocs.io/en/latest/>.

- Update Bash-it to the latest stable/development version:

`bash-it update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stable|dev</span>

- Reload Bash profile (set `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` to non-empty value for an automatic reload):

`bash-it reload`

- Restart Bash:

`bash-it restart`

- Reload Bash profile with enabled error and warning logging:

`bash-it doctor`

- Reload Bash profile with enabled error/warning/entire logging:

`bash-it doctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">errors|warnings|all</span>

- Search for Bash-it aliases/plugins/completions:

`bash-it search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|plugin|completion</span>

- Search for Bash-it aliases/plugins/completions and enable/disable all found items:

`bash-it search --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias|plugin|completion</span>
