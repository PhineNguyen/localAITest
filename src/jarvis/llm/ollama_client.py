import json

import ollama
from src.jarvis.tools.openApp import OpenApp
from src.jarvis.tools.browser import BrowserController


class OllamaClient:
    tools = OpenApp.tools + BrowserController.tools

    def __init__(self, model_name):
        self.model_name = model_name
        self.browser = BrowserController()

    def chat(self, user_text):
        messages = [
            {
                "role": "system",
                "content": (
                "You are a voice assistant named Jarvis. "
                "Respond briefly and naturally. "
                "Use open_app ONLY for desktop applications like notepad, calculator, or file explorer. "
                "Use open_website for anything web-based, including youtube, google, facebook, or any website name. "
                "Use the search_web tool to search Google and get the top search result titles. "
                "Use browser_open_url to open any specific URL in the Chrome browser. "
                "Websites are NEVER opened with open_app."
                ),
            },
            {
                "role": "user",
                "content": user_text,
            },
        ]

        response = ollama.chat(
            model=self.model_name,
            messages=messages,
            tools=self.tools,
            options={"num_predict": 300},
        )

        message = response["message"]
        tool_calls = message.get("tool_calls", [])

        if not tool_calls:
            return message.get("content", "")

        for tool_call in tool_calls:
            function = tool_call["function"]
            function_name = function["name"]
            arguments = function.get("arguments", {})

            if isinstance(arguments, str):
                arguments = json.loads(arguments)

            print(f"Tool call: {function_name} with arguments: {arguments}")

            if function_name == "open_app":
                result = OpenApp.open_app(arguments.get("app_name", ""))
                return result

            if function_name == "open_website":
                result = OpenApp.open_website(arguments.get("website", ""))
                return result
            if function_name == "search_web":
                result = self.browser.search(arguments.get("query", ""))
                return result
            if function_name == "browser_open_url":
                result = self.browser.open_url(arguments.get("url", ""))
                return result

        return "No supported tool was called."
            