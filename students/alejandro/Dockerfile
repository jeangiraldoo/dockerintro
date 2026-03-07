FROM python:3.12-alpine
WORKDIR /app
RUN addgroup -S app && adduser -S app -G app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app
USER app
EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s --retries=5 --start-period=15s\
  CMD wget -qO- http://127.0.0.1:8080/health >/dev/null || exit 1
CMD ["python","/app/app.py"]


# alpine es una imagen de linux ligera
# workdir indica el directorio de trabajo dentro del contenedor
# addgroup y adduser crean un nuevo grupo y usuario para correr sin privilegios, ojo! no correr contenedores root en producción
# COPY copia los archivos necesarios al contenedor
# user agarra al usuario creado para correr la aplicación sin privilegios
# healcheck valida a través de wget (cliente https de aline), flags: -q para modo silencioso, -O- para imprimir el resultado en stdout, y redirige a /dev/null
# puse el healthcheck para que tenga un start-period de 15s, esto es para darle tiempo a la aplicación de arrancar antes de que el healthcheck comience a hacer solicitudes
# cambié el localhost a su IP local (127.0.0.1)
