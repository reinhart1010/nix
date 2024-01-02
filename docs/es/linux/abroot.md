---
layout: page
title: linux/abroot (español)
description: "Utilidad que proporciona completa inmutabilidad y atomicidad mediante transacciones entre 2 estados de partición de la raíz (A⟺B)."
content_hash: 04eb8cea2ebf05a41cc18a26619a7943dcd18e87
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/linux/abroot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abroot

Utilidad que proporciona completa inmutabilidad y atomicidad mediante transacciones entre 2 estados de partición de la raíz (A⟺B).
Las actualizaciones se realizan utilizando imágenes OCI, para asegurar que el sistema está siempre en un estado consistente.
Más información: <https://github.com/Vanilla-OS/ABRoot>.

- Añade paquetes a la imagen local (Nota: después de ejecutar este comando, se necesita aplicar estos cambios):

`sudo abroot pkg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina paquetes de la imagen local (Nota: después de ejecutar este comando, debe aplicar estos cambios):

`sudo abroot pkg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista paquetes en la imagen local:

`sudo abroot pkg list`

- Aplica los cambios en la imagen local (Nota: es necesario reiniciar el sistema para que estos cambios sean aplicados):

`sudo abroot pkg apply`

- Retrocede su sistema al estado anterior:

`sudo abroot rollback`

- Edita/Visualiza los parámetros del kernel:

`sudo abroot kargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">edit|show</span>

- Muestra estado:

`sudo abroot status`

- Muestra ayuda:

`abroot --help`
