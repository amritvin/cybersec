; Print from 10 to 1

BITS 32

extern printf
extern scanf

section .data
    var1 :    dd 10

section .rodata
    var2 :    db "%d", 10, 0

section .text
    global main

    main:
        push ebp
        mov ebp, esp

        .label1:
            push var2
            push DWORD [var1]
            call printf
            push DWORD [var1]
            ;cmp DWORD [var1], 0
            je .label2
            jmp .label1

        .label2:
            xor eax, eax
            leave
            ret
