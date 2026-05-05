from app.services.api_services import get_weather, get_exchange_rate, get_current_time

def ejecutar_tool(nombre: str, parametros: dict) -> str:
    """
    Dispatcher — recibe el nombre de la tool que Claude eligió
    y la ejecuta con los parámetros que Claude determinó.
    """
    import json
    if nombre == "get_weather":
        resultado = get_weather(**parametros)
    elif nombre == "get_exchange_rate":
        resultado = get_exchange_rate(**parametros)
    elif nombre == "get_current_time":
        resultado = get_current_time(**parametros)
    else:
        resultado = {"error": f"Tool {nombre} no encontrada"}

    return json.dumps(resultado, ensure_ascii=False)