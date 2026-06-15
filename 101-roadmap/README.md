# 🗺️ Ruta de Aprendizaje: Ingeniería Inversa

Hoja de ruta progresiva para ir de cero a analizar binarios con soltura.

Cada módulo combina teoría mínima, ejercicios prácticos y enlaces a mis writeups reales.

---

## 🌱 Fase 1: Cimientos

| # | Módulo | ¿Qué aprendes? | Estado |
|---|--------|----------------|--------|
| 01 | [Fundamentos C y ASM](./01-fundamentos.md) | Traducir código C a ensamblador mentalmente | 🚧 Escribiendo |
| 02 | Arquitectura x86-64 | Registros, pila, calling conventions, endianness | 🔜 Pendiente |
| 03 | Herramientas esenciales | Ghidra, Detect It Easy, strings, objdump | 🔜 Pendiente |

## 🌿 Fase 2: Análisis Estático

| # | Módulo | ¿Qué aprendes? | Estado |
|---|--------|----------------|--------|
| 04 | Primeros pasos con Ghidra | Navegar, renombrar funciones, encontrar el main | 🔜 Pendiente |
| 05 | Strings y referencias cruzadas | De un string sospechoso a la función que lo usa | 🔜 Pendiente |
| 06 | Crackmes fáciles sin ejecutar | Resolver validaciones solo leyendo ensamblador | 🔜 Pendiente |

## 🪴 Fase 3: Depuración

| # | Módulo | ¿Qué aprendes? | Estado |
|---|--------|----------------|--------|
| 07 | x64dbg desde cero | Breakpoints, stepping, modificar registros y memoria | 🔜 Pendiente |
| 08 | GDB + pwndbg | Depuración en Linux, misma lógica | 🔜 Pendiente |
| 09 | Parchear binarios | Cambiar `je` por `jmp` y guardar el ejecutable | 🔜 Pendiente |

## 🌳 Fase 4: Técnicas reales

| # | Módulo | ¿Qué aprendes? | Estado |
|---|--------|----------------|--------|
| 10 | Desempaquetado básico | UPX, encontrar OEP, volcar con Scylla | 🔜 Pendiente |
| 11 | Anti-debugging simple | Detectar y burlar IsDebuggerPresent | 🔜 Pendiente |
| 12 | Frida intro | Hooking dinámico sin tocar el binario | 🔜 Pendiente |

---

## 🧭 ¿Cómo usar esta ruta?

1. Ve módulo por módulo en orden
2. No pases al siguiente sin resolver el ejercicio práctico
3. Si te atascas, revisa mis [writeups](../writeups/)
4. Cada módulo tiene una sección "Mis errores" para que no tropieces con lo mismo

## 📚 Recursos complementarios

Toda la awesome list está en [`/awesome-list`](../awesome-list/): libros, cursos, herramientas y canales.