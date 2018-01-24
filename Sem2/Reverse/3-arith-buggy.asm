; Adds two numbers provided as arguments and prints sum

BITS 32

extern atoi
extern printf

section .rodata
    out: db "%d", 10, 0


section .text
    global main

    main:
        push ebp
        mov ebp, esp
        push ebx
        push edi

        mov edi, DWORD [ebp + 12]
        xor eax, eax
        dec eax
        cmp edi, 3
        jne .exit

        mov ebx, DWORD [ebp + 8]
        push DWORD [ebx + 4]
        call atoi
        mov edi, eax

        push DWORD [ebx + 8]
        call atoi
        add edi, eax

        push edi
        push out
        call printf
        xor eax, eax

        .exit:
            pop edi
            pop ebx
            leave
            ret
