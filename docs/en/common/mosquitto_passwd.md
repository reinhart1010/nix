---
layout: page
title: common/mosquitto_passwd (English)
description: "Manage password files for mosquitto."
content_hash: 2c5150ffa867de9ba96f949e46ecbcb0fb72a2bf
---
# mosquitto_passwd

Manage password files for mosquitto.
See also `mosquitto`, the MQTT server that this manages.
More information: <https://mosquitto.org/man/mosquitto_passwd-1.html>.

- Add a new user to a password file (will prompt to enter the password):

`mosquitto_passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create the password file if it doesn't already exist:

`mosquitto_passwd -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Delete the specified username instead:

`mosquitto_passwd -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Upgrade an old plain-text password file to a hashed password file:

`mosquitto_passwd -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/password_file</span>
