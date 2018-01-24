BITS 32

extern printf
extern scanf

section .data
    i   :    dd 1				;1 is store in the value of i

section .rodata
    out :    db "%d", 10, 0			;out contains the format for printing or scanning integers

section .text
    global main

    main:					;this code prints numbers from 1 to 10
        push ebp
        mov ebp, esp				;prologue

        .label1:
            push DWORD [i]			;i is pushed into stack
            push out				;%d is pushed into stack
            call printf				;printf is invoked
            add esp, 8				;pop arguments
            inc DWORD [i]			;inc value of i
            cmp DWORD [i], 10			;i compared with 10
            jg .label2				;if i is less than jump to label1
            jmp .label1

        .label2:
            xor eax, eax			;eax is cleared
            leave				;epilogue
            ret					;eip points to the next instruction
