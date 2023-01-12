import streamlit as st
import os
import pytesseract
from PIL import Image

def procesar_facturas():
    st.set_page_config(page_title="Procesamiento automático de facturas", page_icon=":guardsman:", layout="wide")
    st.title("Procesamiento automático de facturas")

    # Seleccionar el directorio de facturas
    factura_dir = st.selectbox("Seleccione el directorio de facturas", os.listdir())

    # Procesar las facturas
    if st.button("Procesar facturas"):
        # Obtener una lista de todos los archivos en el directorio
        facturas = os.listdir(factura_dir)

        # Recorrer cada archivo en el directorio
        for factura in facturas:
            # Verificar si el archivo es una imagen
            if factura.endswith(".jpg"):
                # Abrir la imagen y usar pytesseract para extraer el texto
                texto = pytesseract.image_to_string(Image.open(factura))

                # Buscar la información relevante en el texto
                # (como el número de factura, el proveedor, la fecha, etc.)
                # y almacenarla en variables
                numero_factura = "TODO: buscar el número de factura en el texto"
                proveedor = "TODO: buscar el nombre del proveedor en el texto"
                fecha = "TODO: buscar la fecha de la factura en el texto"

                # Guardar la información en un archivo CSV o en una base de datos
                with open("facturas.csv", "a") as f:
                    f.write(f"{numero_factura},{proveedor},{fecha}\n")

        st.success("Facturas procesadas!")

if __name__ == '__main__':
    procesar_facturas()
