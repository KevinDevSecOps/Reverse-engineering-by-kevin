# Módulo 01: Fundamentos - C y Ensamblador

## Objetivo
Entender qué instrucciones en ASM se generan a partir de código C simple. Perder el miedo a ver `mov`, `lea`, `call`.

## Recursos Clave (Awesome List)
- [Compiler Explorer (Godbolt.org)](https://godbolt.org/)
- Libro: "C Programming Language" (Kernighan & Ritchie), Capítulos 1-5.

## 🔬 Práctica Guiada (30 min)

### Ejercicio 1: Variables y Aritmética
1.  Ve a [godbolt.org](https://godbolt.org).
2.  Selecciona compilador `x86-64 gcc` y añade flag `-O0`.
3.  Escribe y analiza:

```c
int main() {
    int a = 5;
    int b = 10;
    int c = a + b;
    return c;
}