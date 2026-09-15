import webbrowser
import os

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Factura</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: Arial, sans-serif; 
            padding: 20px 40px; 
            color: #000;
        }
        
        h1.titulo { 
            text-align: center; 
            font-size: 28px; 
            margin-bottom: 20px; 
        }
        
        .numero-factura {
            border: 2px solid #000;
            padding: 8px 15px;
            text-align: right;
            width: 200px;
            margin-left: auto;
            margin-bottom: 20px;
        }
        
        .datos-generales {
            border: 2px solid #000;
            padding: 15px;
            margin-bottom: 25px;
        }
        
        .fila-datos {
            display: flex;
            gap: 30px;
            margin-bottom: 8px;
        }
        
        .campo { flex: 1; }
        .campo-grande { flex: 2; }
        
        .campo label {
            font-weight: bold;
            font-size: 13px;
        }
        
        .campo .valor {
            border-bottom: 1px solid #000;
            min-height: 20px;
            padding: 2px 5px;
        }
        
        h2.subtitulo {
            text-align: center;
            font-size: 16px;
            margin: 20px 0;
        }
        
        .tabla-articulos {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
        }
        
        .tabla-articulos th {
            background-color: #d9d9d9;
            border: 2px solid #000;
            padding: 8px;
            font-size: 13px;
            text-align: left;
        }
        
        .tabla-articulos td {
            border: 2px solid #000;
            padding: 8px;
            min-height: 25px;
        }
        
        .tabla-articulos .col-referencia { width: 20%; }
        .tabla-articulos .col-cantidad { width: 15%; }
        .tabla-articulos .col-descripcion { width: 65%; }
        
        .parte-inferior {
            display: flex;
            gap: 40px;
            margin-top: 30px;
        }
        
        .observaciones {
            flex: 1;
        }
        
        .observaciones label {
            font-weight: bold;
            font-size: 13px;
        }
        
        .observaciones .campo-texto {
            border: 1px solid #000;
            min-height: 80px;
            padding: 8px;
            margin-top: 5px;
        }
        
        .firmas {
            flex: 1;
            display: flex;
            gap: 30px;
        }
        
        .firma-campo {
            text-align: center;
            flex: 1;
        }
        
        .firma-campo label {
            font-weight: bold;
            font-size: 13px;
        }
        
        .firma-linea {
            width: 100%;
            height: 1px;
            background: #000;
            margin-top: 60px;
            margin-bottom: 5px;
        }
        
        .editar-container {
            text-align: right;
            margin-top: 20px;
        }
        
        .btn-editar {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 25px;
            font-size: 14px;
            cursor: pointer;
            border-radius: 4px;
        }
        
        .btn-editar:hover {
            background-color: #45a049;
        }
        
        .btn-editar.modo-guardar {
            background-color: #2196F3;
        }
        
        [contenteditable="true"] {
            background-color: #fffde7;
            outline: 1px dashed #999;
        }
        
        @media print {
            .editar-container { display: none; }
            [contenteditable="true"] {
                background-color: transparent;
                outline: none;
            }
        }
    </style>
</head>
<body>

    <h1 class="titulo">Factura</h1>

    <div class="numero-factura" contenteditable="false">
        <label>NÂº Factura: </label><span>001</span>
    </div>

    <div class="datos-generales" contenteditable="false">
        <div class="fila-datos">
            <div class="campo-grande">
                <label>SeÃ±or(es):</label>
                <div class="valor">&nbsp;</div>
            </div>
            <div class="campo">
                <label>Fecha (D/M/A):</label>
                <div class="valor">&nbsp;</div>
            </div>
            <div class="campo">
                <label>Pedido NÂº:</label>
                <div class="valor">&nbsp;</div>
            </div>
        </div>
        <div class="fila-datos">
            <div class="campo-grande">
                <label>DirecciÃ³n:</label>
                <div class="valor">&nbsp;</div>
            </div>
        </div>
        <div class="fila-datos">
            <div class="campo">
                <label>Transportador:</label>
                <div class="valor">&nbsp;</div>
            </div>
            <div class="campo">
                <label>Conductor:</label>
                <div class="valor">&nbsp;</div>
            </div>
            <div class="campo">
                <label>Placa VehÃ­culo:</label>
                <div class="valor">&nbsp;</div>
            </div>
        </div>
    </div>

    <h2 class="subtitulo">Despachamos los siguientes artÃ­culos</h2>

    <table class="tabla-articulos" contenteditable="false">
        <thead>
            <tr>
                <th class="col-referencia">REFERENCIA</th>
                <th class="col-cantidad">CANTIDAD</th>
                <th class="col-descripcion">DESCRIPCIÃ“N DEL ARTICULO</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
            <tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
        </tbody>
    </table>

    <div class="parte-inferior">
        <div class="observaciones" contenteditable="false">
            <label>Observaciones:</label>
            <div class="campo-texto">&nbsp;</div>
        </div>
        <div class="firmas">
            <div class="firma-campo" contenteditable="false">
                <label>Despachado por:</label>
                <div class="firma-linea"></div>
            </div>
            <div class="firma-campo" contenteditable="false">
                <label>Recibido por:</label>
                <div class="firma-linea"></div>
            </div>
        </div>
    </div>

    <div class="editar-container">
        <button class="btn-editar" id="btnEditar" onclick="toggleEditar()">Editar</button>
    </div>

    <script>
        function toggleEditar() {
            const btn = document.getElementById('btnEditar');
            const campos = document.querySelectorAll('[contenteditable]');
            
            if (btn.textContent === 'Editar') {
                campos.forEach(c => c.contentEditable = 'true');
                btn.textContent = 'Guardar';
                btn.classList.add('modo-guardar');
            } else {
                campos.forEach(c => c.contentEditable = 'false');
                btn.textContent = 'Editar';
                btn.classList.remove('modo-guardar');
            }
        }
    </script>

</body>
</html>
"""

def generar_factura():
    nombre_archivo = "factura_output.html"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    ruta_absoluta = os.path.abspath(nombre_archivo)
    print(f"Factura generada: {ruta_absoluta}")
    
    webbrowser.open(f"file://{ruta_absoluta}")

if __name__ == "__main__":
    generar_factura()
