# Documento de Remisión - Generador de Factura

Generador de facturas en formato HTML/CSS con Python.

## Archivos

- actura.py - Script principal que genera la factura
- actura_output.html - Factura generada (resultado)

## Uso

`ash
python factura.py
`

Esto genera actura_output.html y lo abre automáticamente en el navegador.

## Funcionalidades

- Título "Factura" centrado
- Recuadro con N° de Factura
- Campos: Señor(es), Fecha, Pedido, Dirección, Transportador, Conductor, Placa
- Tabla de artículos (Referencia, Cantidad, Descripción)
- Sección de Observaciones
- Campos de firma (Despachado por / Recibido por)
- Botón **Editar** para modificar campos directamente en el navegador
- Exportar como PDF: Ctrl+P → Guardar como PDF

## Requisitos

- Python 3.x
- Navegador web