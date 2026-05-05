# 🤖 Telegram Agent Bot (Español)

---

## 📌 Descripción

Bot de Telegram con agente inteligente que consulta APIs reales en tiempo real.
Escribe en lenguaje natural y el agente decide qué herramientas usar para responder.
Cambia automáticamente entre polling (local) y webhook (producción en Railway).

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo de IA.

**GitHub:** https://github.com/SergioArdCr/telegram-agent-bot

---

## 🛠️ Tecnologías

| Librería | Uso |
|---|---|
| `FastAPI` | Framework web para recibir el webhook de Telegram |
| `python-telegram-bot` | Interacción con la API de Telegram |
| `anthropic` | SDK para Claude y tool calling |
| `httpx` | Llamadas HTTP a APIs externas |
| `Docker` | Contenedor de la aplicación |

---

## 📁 Estructura

```
telegram-agent-bot/
├── app/
│   ├── agent/
│   │   ├── tools.py          # Definición de tools para Claude
│   │   ├── executor.py       # Ejecución de cada tool con httpx
│   │   └── agent.py          # Agentic loop
│   ├── bot/
│   │   └── handlers.py       # Recibe mensajes, llama al agente
│   └── main.py               # FastAPI + webhook/polling automático
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── requirements.txt
```

---

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/telegram-agent-bot.git
cd telegram-agent-bot

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Levantar contenedor
docker-compose up --build
```

---

## 🔐 Variables de entorno

```env
TELEGRAM_TOKEN=tu_token_de_botfather
ANTHROPIC_API_KEY=tu_api_key
WEBHOOK_URL=   # Vacío en local, URL pública de Railway en producción
```

---

## 🛠️ Tools disponibles

| Tool | Descripción | API usada |
|---|---|---|
| `get_weather` | Clima actual de una ciudad | wttr.in (pública) |
| `get_exchange_rate` | Conversión entre monedas | open.er-api.com (pública) |
| `get_current_time` | Hora actual en una ciudad | worldtimeapi.org (pública) |

---

## 💬 Ejemplos de uso

```
"¿Cuánto son 200 dólares en pesos colombianos?"
→ Agente llama get_exchange_rate("USD", "COP", 200)
→ Responde con el valor actual

"¿Qué clima hace en Medellín?"
→ Agente llama get_weather("Medellín")
→ Responde con temperatura, sensación y condición

"¿Cuál es el clima y la hora en Madrid?"
→ Agente llama get_weather("Madrid") Y get_current_time("Madrid")
→ Responde con ambos resultados en un solo mensaje
```

---

## 🔄 Cómo funciona el agente

```
Usuario escribe en Telegram
        ↓
Handler recibe el mensaje
        ↓
Claude analiza — ¿necesito una tool?
        ↓
SÍ → Claude devuelve tool_use con parámetros
        ↓
executor.py ejecuta la tool con httpx
        ↓
Resultado se devuelve a Claude
        ↓
Claude formula respuesta final
        ↓
Bot responde en Telegram
```

El loop se repite hasta que Claude decide que tiene toda la información necesaria (`stop_reason == "end_turn"`).

---

## 🚀 Deploy en Railway

### Variables requeridas

```env
TELEGRAM_TOKEN=    # Token de BotFather
ANTHROPIC_API_KEY= # API key de Anthropic
WEBHOOK_URL=       # URL pública asignada por Railway
```

### Configuración

- **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Verificar webhook activo

```bash
curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo
```

---

## 💡 Aprendizajes clave

- **Tool calling** — darle herramientas a Claude para actuar en el mundo real
- **Agentic loop** — ciclo razonamiento → acción → resultado → respuesta
- `stop_reason == "tool_use"` vs `stop_reason == "end_turn"` — cómo saber cuándo Claude terminó
- Claude puede usar múltiples tools en una sola pregunta
- Diferencia entre un chatbot (solo responde) y un agente (responde y actúa)
- Integración de bot de Telegram con agente LLM

---

---

# 🤖 Telegram Agent Bot (English)

---

## 📌 Description

Telegram bot with an intelligent agent that queries real APIs in real time.
Write in natural language and the agent decides which tools to use to respond.
Automatically switches between polling (local) and webhook (Railway production).

Built as part of a Python learning plan focused on AI development.

**GitHub:** https://github.com/SergioArdCr/telegram-agent-bot

---

## 🛠️ Tech Stack

| Library | Usage |
|---|---|
| `FastAPI` | Web framework to receive Telegram webhook |
| `python-telegram-bot` | Interaction with Telegram API |
| `anthropic` | SDK for Claude and tool calling |
| `httpx` | HTTP calls to external APIs |
| `Docker` | Application container |

---

## 📁 Structure

```
telegram-agent-bot/
├── app/
│   ├── agent/
│   │   ├── tools.py          # Tool definitions for Claude
│   │   ├── executor.py       # Tool execution with httpx
│   │   └── agent.py          # Agentic loop
│   ├── bot/
│   │   └── handlers.py       # Receives messages, calls the agent
│   └── main.py               # FastAPI + automatic webhook/polling
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── requirements.txt
```

---

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/telegram-agent-bot.git
cd telegram-agent-bot

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your values

# Start container
docker-compose up --build
```

---

## 🔐 Environment Variables

```env
TELEGRAM_TOKEN=your_botfather_token
ANTHROPIC_API_KEY=your_api_key
WEBHOOK_URL=   # Empty locally, Railway public URL in production
```

---

## 🛠️ Available Tools

| Tool | Description | API used |
|---|---|---|
| `get_weather` | Current weather for a city | wttr.in (public) |
| `get_exchange_rate` | Currency conversion | open.er-api.com (public) |
| `get_current_time` | Current time in a city | worldtimeapi.org (public) |

---

## 💬 Usage Examples

```
"How much is 200 dollars in Colombian pesos?"
→ Agent calls get_exchange_rate("USD", "COP", 200)
→ Responds with current value

"What's the weather in Medellín?"
→ Agent calls get_weather("Medellín")
→ Responds with temperature, feels like and condition

"What's the weather and time in Madrid?"
→ Agent calls get_weather("Madrid") AND get_current_time("Madrid")
→ Responds with both results in one message
```

---

## 🔄 How the agent works

```
User writes in Telegram
        ↓
Handler receives the message
        ↓
Claude analyzes — do I need a tool?
        ↓
YES → Claude returns tool_use with parameters
        ↓
executor.py runs the tool with httpx
        ↓
Result is sent back to Claude
        ↓
Claude formulates final response
        ↓
Bot replies in Telegram
```

The loop repeats until Claude decides it has all the information it needs (`stop_reason == "end_turn"`).

---

## 🚀 Deploy on Railway

### Required Variables

```env
TELEGRAM_TOKEN=    # BotFather token
ANTHROPIC_API_KEY= # Anthropic API key
WEBHOOK_URL=       # Public URL assigned by Railway
```

### Configuration

- **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Verify active webhook

```bash
curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo
```

---

## 💡 Key Learnings

- **Tool calling** — giving Claude tools to act in the real world
- **Agentic loop** — reasoning → action → result → response cycle
- `stop_reason == "tool_use"` vs `stop_reason == "end_turn"` — knowing when Claude is done
- Claude can use multiple tools in a single question
- Difference between a chatbot (only responds) and an agent (responds and acts)
- Integrating a Telegram bot with an LLM agent
