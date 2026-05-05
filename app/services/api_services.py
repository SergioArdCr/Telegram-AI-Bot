import httpx

BASE_URL_EXCHANGE = "https://open.er-api.com/v6/latest/"

def get_weather(ciudad: str) -> dict:
    """
    wttr.in es una API pública de clima — no necesita key.
    format=j1 devuelve JSON estructurado.
    """
    try:
        response = httpx.get(
            f"https://wttr.in/{ciudad}?format=j1",
            timeout=10
        )
        data = response.json()
        current = data["current_condition"][0]
        return {
            "ciudad": ciudad,
            "temperatura_c": current["temp_C"],
            "sensacion_c": current["FeelsLikeC"],
            "descripcion": current["weatherDesc"][0]["value"],
            "humedad": current["humidity"]
        }
    except Exception as e:
        return {"error": f"No pude obtener el clima de {ciudad}: {str(e)}"}

def get_exchange_rate(moneda_origen: str, moneda_destino: str, monto: float) -> dict:
    """
    Usa la misma API que ya conoces de tu proyecto anterior.
    """
    try:
        response = httpx.get(
            f"{BASE_URL_EXCHANGE}{moneda_origen.upper()}",
            timeout=10
        )
        data = response.json()
        rate = data["rates"][moneda_destino.upper()]
        resultado = round(monto * rate, 2)
        return {
            "moneda_origen": moneda_origen.upper(),
            "moneda_destino": moneda_destino.upper(),
            "monto_original": monto,
            "resultado": resultado,
            "tasa": rate
        }
    except Exception as e:
        return {"error": f"No pude convertir {moneda_origen} a {moneda_destino}: {str(e)}"}

def get_current_time(ciudad: str) -> dict:
    """
    worldtimeapi.org — API pública de zonas horarias.
    Mapeo básico de ciudades a zonas horarias.
    """
    zonas = {
        "bogotá": "America/Bogota",
        "bogota": "America/Bogota",
        "medellín": "America/Bogota",
        "medellin": "America/Bogota",
        "madrid": "Europe/Madrid",
        "new york": "America/New_York",
        "nueva york": "America/New_York",
        "london": "Europe/London",
        "londres": "Europe/London",
        "tokio": "Asia/Tokyo",
    }
    zona = zonas.get(ciudad.lower(), "America/Bogota")
    try:
        response = httpx.get(
            f"https://timeapi.io/api/Time/current/zone?timeZone={zona}",
            timeout=10
        )
        data = response.json()
        return {
            "ciudad": ciudad,
            "hora": data["time"],
            "zona_horaria": zona
        }
    except Exception as e:
        return {"error": f"No pude obtener la hora de {ciudad}: {str(e)}"}