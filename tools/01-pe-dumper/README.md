# 01 - PE Section Dumper

## 🎯 Objetivo
Entender la estructura de un ejecutable Windows parseando sus secciones sin usar una herramienta gráfica. Saber qué es .text, .data, .rdata y qué permisos tienen.

## 📦 Dependencias
```bash
pip install pefile
🚀 Uso

```bash
python pe_dumper.py programa.exe
```

📤 Salida esperada

```
Name      VirtualAddress    RawSize     Permissions
---------------------------------------------------
.text     0x00001000        0x0000C400  0x60000020
.rdata    0x0000E000        0x00003A00  0x40000040
.data     0x00012000        0x00000800  0xC0000040
```

🧠 ¿Qué aprendí?

· La diferencia entre VirtualAddress (en memoria) y RawSize (en disco)
· Los permisos típicos: .text ejecutable, .rdata solo lectura
· Cómo pefile abstrae la estructura PE de Windows
