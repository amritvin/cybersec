extern fclose
extern fopen
extern fread
extern memset
extern printf

%define NUM1 20
%define NUM2 1

section .rodata
    error         : db "Cannot open file! Exiting!", 10, 0
    open_mode     : db "r", 0
    output_format : db "%s", 0
    usage         : db "Usage: %s file", 10, 0

section .bss
    buffer : resb NUM1 + 1
    fn     : resd 1
    fh     : resd 1

section .text
    global main

    main:
        push ebp
        mov ebp, esp

        mov edi, DWORD [ebp + 8]	;conatins argc
        mov esi, DWORD [ebp + 12]	;contains *argv address

        cmp edi, 2			;there should be two command line arguments; the executable file and file to be opened 
        jne .label1

        mov eax, [esi + 4]		;argv[1] is pushed into eax; the filename in this case
        mov DWORD [fn], eax		;and that is stored into fn

        push open_mode
        push DWORD [fn]			
        call fopen			;the file is opened
        add esp, 8
        test eax, eax			;contains zero if the file cant be opened;zero flag s set if eax contains zero;eax contains zero if 						 fopen fails; eax containd the file pointer
        jz .label2

        mov [fh], eax			;the file pointer is stored into fh

        push NUM1			;size of the buffer is defined
        push 0				;every element is set to 0
        push buffer			;the arrat
        call memset			;memset allocates o to the buffer of size 20
        add esp, 12

        push DWORD [fh]			;pushes the file pointer
        push NUM1			
        push NUM2
        push buffer
        call fread			;the data is read from the file into the buffer with the given size(NUM1) and eaxh char is of size 1 						 byte as its character
        add esp, 16
        mov BYTE [buffer + NUM1], 0

        push buffer			
        push output_format
        call printf			;the data read from the file is printed in the terminal
        add esp, 8

        push DWORD [fh]
        call fclose			;the file is closed
        add esp, 4
        mov eax, 0
        jmp .label3

        .label1:
            push DWORD [esi]
            push usage			;if more than one file names are sepcified or if its not specified, "Usage: %s file" is printed
            call printf
            add esp, 8
            mov eax, 0
            jmp .label3

        .label2:
            push error
            call printf			;the error messasge "Cannot open file! Exiting!" is printed
            add esp, 4
            mov eax, 1
            jmp .label3

        .label3:
            leave
            ret
