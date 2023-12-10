# Proyecto conciliaciones bancarias para Moniic
** Integrantes del equipo **
> Alan
Luis
Sari
Bruno
Georgie
Sandoval Gil Gael Sebastián
...

### Descripción del proyecto
Esta API proporciona servicios para realizar conciliaciones de facturas en los esquemas de PPD (Pago en Parcialidades Diferidas) y PUE (Pago en Una Exhibición) en el contexto de facturación electrónica. La conciliación de facturas es crucial para asegurar la integridad y coherencia de los registros financieros.

### Funcionalidades
1. Conciliación de Facturas PPD
Permite conciliar facturas que han sido liquidadas en parcialidades diferidas, asegurando la correcta correspondencia entre las transacciones registradas y los distintos movimientos bancarios realizados para liquidarla.
2. Conciliación de Facturas PUE
Facilita la conciliación de facturas en el esquema de PUE, garantizando la coincidencia entre los registros contables y los pagos realizados en una única exhibición.
3. Consulta de Conciliaciones (Por definir)
Ofrece la posibilidad de consultar el estado de las conciliaciones realizadas, proporcionando detalles sobre los resultados obtenidos y permitiendo un seguimiento efectivo.

### Uso
** Endpoints Disponibles **
- POST "/moniic/v1/ppd": Realiza la conciliación de la factura PPD.
- POST "/moniic/v1/pue": Realiza la conciliación de la factura PUE.
- GET "/moniic/v1/bitacora": Obtiene un listado de todas las conciliaciones realizadas. (Por definir)

** Ejemplo de uso **
Conciliación de Factura PPD

	POST /moniic/v1/ppd
	Content-Type: application/json

	{
		"invoice_type": "PPD",
		"invoice_uuid": "SAHDFASJKLDHFS56654D5SFD64F6S54F6"
	}

### Requisitos
- Python 3x
- Flask, Flask-RESTful