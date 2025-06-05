import gradio as gr
import requests

MCP_SERVER_URL = "http://127.0.0.1:8000/"  # or your remote MCP tool

def query_mcp(input_text):
    try:
        res = requests.post(MCP_SERVER_URL, json={"input": input_text})
        return res.json().get("output", "No response.")
    except Exception as e:
        return f"Error: {str(e)}"

gr.Interface(fn=query_mcp, inputs="text", outputs="text", title="InboxPilot MCP Client").launch()
