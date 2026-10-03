# Second Shift · Catálogo y finanzas

## Sistema de finanzas (`finanzas/`)

Sistema administrativo para el negocio de uniformes, inspirado en las funciones de
[Fina](https://producto.finapartner.com/) (inventario, ventas, cuentas por cobrar y por pagar,
rentabilidad en tiempo real y multimoneda con tasa BCV), adaptado a la venta de uniformes
escolares, médicos y corporativos.

**Versión en la nube (recomendada):** publicada en claude.ai como Artifact con base de datos
compartida: https://claude.ai/artifact/38Kygx6bYRGQnQpzAtcjqf — los datos se guardan en la nube
y todas las personas con acceso ven los cambios en vivo. Se comparte desde el menú **Compartir**
de la página. Tras modificar la app, regenera el archivo con `python3 finanzas/build-nube.py` y
vuelve a publicar `finanzas/nube.html`.

**Versión local:** abre `finanzas/index.html` en el navegador (doble clic). No necesita
instalación ni internet; los datos quedan en ese navegador. Para probarla, en el Panel pulsa
**Cargar datos de ejemplo**.

### Módulos

| Módulo | Qué hace |
| --- | --- |
| **Panel** | Ventas, utilidad neta, gastos, dinero disponible, por cobrar (y vencido), por pagar, valor del inventario, gráfico de 6 meses, más vendidos, pedidos por entregar y stock bajo. |
| **Ventas** | Notas de entrega con varios productos/tallas, descuento, pago de contado o a crédito, descuento automático del inventario, impresión y envío por WhatsApp. |
| **Pedidos** | Encargos para colegios/empresas con personalización (bordado, logo, nombre), fecha de entrega, estados (Cotizado → Confirmado → En producción → Listo → Entregado), abonos; al entregar se convierten en venta. |
| **Inventario** | Productos por categoría e institución, stock por talla, costo, precio y margen, stock mínimo, ajustes/entradas de producción con historial de movimientos. |
| **Compras y gastos** | Compras de mercancía (suben stock y actualizan costo) y gastos por categoría (telas, costura, bordado, nómina, alquiler…), en $, Bs o €, pagados o a crédito. |
| **Por cobrar / Por pagar** | Saldos pendientes, vencimientos, antigüedad de deuda (1-30, 31-60, 61-90, +90 días), saldo por cliente, recordatorio por WhatsApp con monto en Bs a tasa del día. |
| **Caja y bancos** | Cuentas en $, Bs o € (efectivo, banco, pago móvil, Zelle, Binance…), saldo en vivo, libro de movimientos, aportes/retiros y transferencias o cambio de divisas. |
| **Clientes / Proveedores** | Fichas con RIF, teléfono, total comprado y saldo pendiente. |
| **Reportes** | Estado de resultados (ventas, costo de lo vendido, utilidad bruta, gastos por categoría, utilidad neta), flujo de caja, rentabilidad por producto, ventas por institución y por cliente, unidades por talla. Exportación CSV (Excel). |
| **Configuración** | Tasa BCV ($ y €) manual o consultada en internet, historial de tasas, datos del negocio, cuentas, tallas y categorías, respaldo/restauración. |

### Multimoneda

Todo se registra en dólares y se puede ver en $, Bs o € con el selector superior. Cada cobro o
pago en Bs guarda la tasa del día, así el diferencial cambiario no altera lo ya cobrado, y los
saldos pendientes se muestran en Bs a la tasa actual.

### Importante: respaldo

En la versión local los datos se guardan en el navegador del equipo donde se usa (localStorage);
para pasarlos a la nube, descarga el respaldo allí y restáuralo en la versión en la nube. Descarga un respaldo
con frecuencia desde **Configuración → Descargar respaldo** y guárdalo en Drive o en tu correo;
con ese archivo puedes restaurar o mover la información a otro equipo.
