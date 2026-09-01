import os
import glob
import shutil
import webbrowser
from urllib.parse import quote_plus, urlparse

class OpenApp:
    APP_ALIASES = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "file explorer": "explorer.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "powershell": "powershell.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "powerpoint": "powerpnt.exe",
        "outlook": "outlook.exe",
        "edge": "msedge.exe",
        "chrome": "chrome.exe",
        "steam": "steam.exe",
    }
    
    WEBSITE_ALIASES = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
    }

    _start_menu_cache = None

    tools = [
        {
            "type": "function",
            "function": {
                "name": "open_app",
                "description": "Open an application on Windows by name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_name": {
                            "type": "string",
                            "description": "The name of the application to open"
                        }
                    },
                    "required": ["app_name"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "open_website",
                "description": "Open a website in the default browser",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "website": {
                            "type": "string",
                            "description": (
                                "Website name, domain, or URL. Examples: "
                                "Google, YouTube, github.com"
                            )
                        }
                    },
                    "required": ["website"]
                }
            }
        }
    ]

    @staticmethod
    def _scan_start_menu():
        """Return installed Start Menu apps as name-to-shortcut mappings."""
        if OpenApp._start_menu_cache is not None:
            return OpenApp._start_menu_cache

        apps = {}
        search_paths = []

        program_data = os.environ.get("ProgramData")
        app_data = os.environ.get("APPDATA")

        if program_data:
            search_paths.append(
                os.path.join(
                    program_data,
                    r"Microsoft\Windows\Start Menu\Programs",
                )
            )

        if app_data:
            search_paths.append(
                os.path.join(
                    app_data,
                    r"Microsoft\Windows\Start Menu\Programs",
                )
            )

        for base_path in search_paths:
            if not os.path.isdir(base_path):
                continue

            pattern = os.path.join(base_path, "**", "*.lnk")

            for shortcut_path in glob.glob(pattern, recursive=True):
                app_name = os.path.splitext(
                    os.path.basename(shortcut_path)
                )[0].casefold()
                apps[app_name] = shortcut_path

        OpenApp._start_menu_cache = apps
        return apps

    @staticmethod
    def open_app(app_name: str) -> str:
        """Open a Windows application by alias, PATH, or Start Menu name."""
        if not isinstance(app_name, str):
            return "Application name must be text."

        app_name = app_name.strip()

        if not app_name:
            return "Application name required."

        app_key = app_name.casefold()
        executable = OpenApp.APP_ALIASES.get(app_key)

        if not executable:
            executable = shutil.which(app_name)

        if not executable:
            apps = OpenApp._scan_start_menu()
            executable = apps.get(app_key)

            if not executable:
                for name, path in apps.items():
                    if app_key in name:
                        executable = path
                        break

        if not executable:
            return f"Couldn't find application: {app_name}"

        try:
            os.startfile(executable)
            return f"Opened {app_name}."
        except OSError as error:
            return f"Couldn't open {app_name}: {error}"

    @staticmethod
    def open_website(website: str) -> str:
        """Open a website alias, domain, URL, or Google search term."""
        if not isinstance(website, str):
            return "Website name must be text."

        website = website.strip()

        if not website:
            return "Website name required."

        website_key = website.casefold()

        if website_key in OpenApp.WEBSITE_ALIASES:
            url = OpenApp.WEBSITE_ALIASES[website_key]
        elif website.startswith(("http://", "https://")):
            url = website
        elif "." in website and " " not in website:
            url = f"https://{website}"
        else:
            search_url = (
                "https://www.google.com/search?q="
                + quote_plus(website)
            )
            url = search_url

        parsed_url = urlparse(url)

        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            return f"Invalid website: {website}"

        try:
            opened = webbrowser.open(url)

            if opened:
                return f"Opened {website}."

            return f"Couldn't open website: {website}"
        except OSError as error:
            return f"Couldn't open website: {error}"
        