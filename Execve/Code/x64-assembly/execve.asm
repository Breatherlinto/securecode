bits 64                 

section .data           ; section for data declaration 
        bin:    db "/bin/sh",0          ;
        arg0:   db "/bin/sh",0
        arg1:   db "-c",0
        arg2:   db "ls -al /etc",0
        ;initalisation of array argv 
argv:
        dq arg0
        dq arg1
        dq arg2
        dq 0

section .text ;initalisation of begin for programm
        global _start

_start:         ; Beginn of Orders
    ; execve("/bin/sh", argv, 0)

        mov rax, 59        ; 59 execve syscall register rax for syscall
        mov rdi, arg0      ; filename bin/sh
        mov rsi, argv      ; weist argv array in rsi 
        mov rdx, 0         ; null deklaration 
        syscall
; section for ending code with exit 60
        mov rax, 60
        mov rdi, 0
        syscall 
