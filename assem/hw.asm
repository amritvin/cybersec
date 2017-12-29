extern printf
section .text
global main
main:
	push ebp
	mov ebp, esp
	push msg
	call printf 
	add esp, 4
	mov eax, 2
	mov ebx, 4
	add eax,ebx
	push eax
	push am
	call printf 
	add esp, 8
	leave
	ret
section .data
	msg db 'Math Calculator ',13,10,0
	am db 'sum is %d',13,10,0
