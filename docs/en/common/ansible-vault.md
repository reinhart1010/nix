---
layout: page
title: common/ansible-vault (English)
description: "Encrypts & decrypts values, data structures and files within Ansible projects."
content_hash: c894bebdbc34e8e27b316a2a08d6a2f7d87c93bd
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-vault.html
    icon: bi bi-globe
---
# ansible-vault

Encrypts & decrypts values, data structures and files within Ansible projects.
More information: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Create a new encrypted vault file with a prompt for a password:

`ansible-vault create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>

- Create a new encrypted vault file using a vault key file to encrypt it:

`ansible-vault create --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>

- Encrypt an existing file using an optional password file:

`ansible-vault encrypt --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>

- Encrypt a string using Ansible's encrypted string format, displaying interactive prompts:

`ansible-vault encrypt_string`

- View an encrypted file, using a password file to decrypt:

`ansible-vault view --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>

- Re-key already encrypted vault file with a new password file:

`ansible-vault rekey --vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_password_file</span>` --new-vault-password-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_password_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vault_file</span>
