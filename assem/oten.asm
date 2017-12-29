extern printf 
section .text
global main
main:
push ebp
mov ebp,esp
mov ebx, 1
up:cmp ebx,11
je dwn	
   push ebx
   push msg
   call printf
   add bx,1
   pop eax
   pop eax
jmp up
dwn:
   leave 
   ret
section .data
msg db "%d",13,10,0
