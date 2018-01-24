; Someone tried learning some arithmetic but got a strange error

BITS 32

extern printf

section .rodata
    out: db "%d", 10, 0

section .text

global main

    main:
        push ebp
        mov ebp, esp

        mov eax, 1000
        xor edx, edx
        xor ecx, ecx
        idiv ecx

        push eax
        push out
        call printf

        xor eax, eax
        leave
        ret
