
#### `tools/01-pe-dumper/pe_dumper.py`

```python
#!/usr/bin/env python3
"""
PE Section Dumper - Muestra las secciones de un ejecutable PE
Parte de Reverse-Engineering-By-KevinCK
"""

import sys
import pefile


def analizar_pe(ruta: str) -> None:
    """Carga un PE y muestra información de sus secciones."""

    try:
        pe = pefile.PE(ruta)
    except Exception as e:
        print(f"[!] Error al abrir {ruta}: {e}")
        sys.exit(1)

    print(f"\n📦 Archivo: {ruta}")
    print(f"🖥️  Máquina: {hex(pe.FILE_HEADER.Machine)}")
    print(f"📄 Secciones: {pe.FILE_HEADER.NumberOfSections}\n")

    # Cabecera de la tabla
    print(f"{'Name':<10} {'VirtualAddress':>14} {'RawSize':>10} {'Permissions':>12}")
    print("-" * 48)

    for section in pe.sections:
        name = section.Name.decode().strip('\x00')
        va = section.VirtualAddress
        raw = section.SizeOfRawData
        perm = section.Characteristics

        print(f"{name:<10} 0x{va:08X}       0x{raw:06X}   0x{perm:08X}")

    print("\n✅ Análisis completado.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Uso: python {sys.argv[0]} <ejecutable.exe>")
        sys.exit(1)

    analizar_pe(sys.argv[1])