tools = [
    {
        "name": "get_weather",
        "description": "Obtiene el clima actual de una ciudad",
        "input_schema": {
            "type": "object",
            "properties": {
                "ciudad": {
                    "type": "string",
                    "description": "Nombre de la ciudad, ej: Bogotá, Medellín"
                }
            },
            "required": ["ciudad"]
        }
    },
    {
        "name": "get_exchange_rate",
        "description": "Convierte un monto de una moneda a otra. Útil para saber cuánto equivale en pesos colombianos, euros, etc.",
        "input_schema": {
            "type": "object",
            "properties": {
                "moneda_origen": {
                    "type": "string",
                    "description": "Código de moneda origen, ej: USD, EUR"
                },
                "moneda_destino": {
                    "type": "string",
                    "description": "Código de moneda destino, ej: COP, EUR"
                },
                "monto": {
                    "type": "number",
                    "description": "Cantidad a convertir"
                }
            },
            "required": ["moneda_origen", "moneda_destino", "monto"]
        }
    },
    {
        "name": "get_current_time",
        "description": "Obtiene la hora actual en una ciudad o zona horaria",
        "input_schema": {
            "type": "object",
            "properties": {
                "ciudad": {
                    "type": "string",
                    "description": "Nombre de la ciudad, ej: Bogotá, Madrid"
                }
            },
            "required": ["ciudad"]
        }
    }
]