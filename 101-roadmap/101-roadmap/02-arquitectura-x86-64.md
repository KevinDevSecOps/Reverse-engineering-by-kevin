```markdown
# Módulo 02: Arquitectura x86-64

## 🎯 Objetivo
Entender los registros, la pila, el orden de los bytes y cómo se pasan argumentos a funciones. Sin esto, el ensamblador es un galimatías.

---

## 🧠 Registros esenciales

Imagínalos como variables globales del procesador. En x86-64 tienes:

| Registro | Propósito típico | ¿Qué guarda? |
|----------|------------------|---------------|
| `RAX` | Valor de retorno | Lo que devuelve una función |
| `RDI, RSI, RDX, RCX, R8, R9` | Argumentos | Los 6 primeros parámetros de una función |
| `RSP` | Stack Pointer | Apunta a la cima de la pila |
| `RBP` | Base Pointer | Marca la base del marco de pila actual |
| `RIP` | Instruction Pointer | Dirección de la próxima instrucción |

> 💡 **Dato clave**: Si una función tiene más de 6 argumentos, los extra van por la pila.

---

## 🥞 La pila (stack)

Crece **hacia abajo** (direcciones más bajas). `push` resta a `RSP`, `pop` suma.

```

Direcciones altas
┌──────────────┐
│   args extra │  <- RBP + 16
├──────────────┤
│   ret addr   │  <- RBP + 8
├──────────────┤
│  saved RBP   │  <- RBP (Base Pointer)
├──────────────┤
│  vars locales│  <- RBP - X
├──────────────┤
│     ...      │  <- RSP (Stack Pointer, abajo del todo)
└──────────────┘
Direcciones bajas

```

---

## 📦 Endianness (orden de bytes)

x86-64 usa **little-endian**: el byte menos significativo va primero.

```

Valor: 0x12345678
En memoria little-endian: 78 56 34 12

```

> 🔍 En Ghidra o x64dbg verás los bytes al revés. Es normal, no está roto.

---

## 📞 Calling conventions

En **Windows** y **Linux** (System V AMD64) los argumentos van en registros distintos:

| Argumento | Windows | Linux |
|-----------|---------|-------|
| 1º | RCX | RDI |
| 2º | RDX | RSI |
| 3º | R8 | RDX |
| 4º | R9 | RCX |
| 5º | Pila | R8 |
| 6º | Pila | R9 |

> ⚠️ Importantísimo al analizar malware Windows vs binarios Linux.

---

## 🔬 Ejercicio práctico

Ve a [godbolt.org](https://godbolt.org) con `x86-64 gcc -O0` y analiza:

```c
int sumar(int a, int b, int c, int d, int e, int f, int g) {
    return a + b + c + d + e + f + g;
}

int main() {
    return sumar(1, 2, 3, 4, 5, 6, 7);
}
```

Misiones:

1. ¿En qué registros se pasan los 6 primeros argumentos?
2. ¿Cómo se pasa el 7º argumento (g=7)?
3. Encuentra el add que suma a + b. ¿Qué registros suma?

---

⚠️ Mis errores de principiante

"Al principio no entendía por qué a veces los argumentos estaban en RCX y otras en RDI. Resulta que depende del sistema operativo. Pasé horas debuggeando un binario de Windows con documentación de Linux. Desde entonces siempre confirmo la calling convention antes de analizar."

"También flipé viendo bytes al revés en el hexdump. Pensé que Ghidra estaba mal. No: es little-endian. 0xDEADBEEF se ve como EF BE AD DE."

---
