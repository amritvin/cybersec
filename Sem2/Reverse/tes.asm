extern printf
extern scanf
%define NUM1 20
%define NUM2 1
section .rodata                             ; start of data section
    hello_world: db "Hello, world!", 10, 0  ; string we wish to print out

section .text
	global main
	main:
		push ebp
		mov ebp,esp
		push hello_world
		add esp,4
		leave
		ret
