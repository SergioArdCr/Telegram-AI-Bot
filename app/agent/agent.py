import anthropic
import os
from app.agent.tools import tools
from app.agent.executor import ejecutar_tool

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Eres un asistente útil con acceso a herramientas de clima, 
conversión de divisas y hora actual. 
Responde siempre en español de manera concisa y amigable.
Usa las herramientas cuando el usuario necesite información en tiempo real."""

def ejecutar_agente(mensaje: str) -> str:
    """
    Agentic loop — corre hasta que Claude decide que terminó.
    
    stop_reason == "tool_use"  → Claude quiere usar una tool
    stop_reason == "end_turn"  → Claude tiene la respuesta final
    """
    messages = [{"role": "user", "content": mensaje}]

    while True:
        response = claude.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        # Claude terminó — devuelve respuesta final
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Claude quiere usar una tool
        if response.stop_reason == "tool_use":
            # Agrega respuesta de Claude al historial
            messages.append({
                "role": "assistant",
                "content": response.content
            })

            # Ejecuta todas las tools que Claude pidió
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    resultado = ejecutar_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": resultado
                    })

            # Devuelve los resultados a Claude
            messages.append({
                "role": "user",
                "content": tool_results
            })