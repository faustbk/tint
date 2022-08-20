import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9447710"))
API_HASH = getenv("API_HASH", "bfbdd55dfcc54fe2832d1ff4bbe234e2")
BOT_TOKEN = getenv("BOT_TOKEN", "5423656818:AAFLBB-Lht8dLXRZy0TpD85uTrK8S6FGz6U")
DURATION_LIMIT = int(getenv("E_V_Abot", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQAZrFmew2qg6fXlzeqZiuI5qBzZSNwkSkvdouU16e5y8ZCWU1RUtejuo5c5L9Hru7v3o0-m_6rV2muYbdr7ApMpaR6__Knq1cU3KPjLAN8uiRWA1RlZk-j7JRB44VGOZ0OEuhsrObao2qh14foHNndLvJdhBfrYi7jppVPLidXI8B5XDw9AX9HV_S05GAb16TERMsrTk5fiNelRSozXJIG2X1XUdpXm0I7gawLvaf6wRpqodo8Z0zEEBh-7UD_RFyOMcuGA92K0uWCuDkCOwwz19p1j7ESMtox2AAYU8sUefZ8OnGbpWOPXIj9DwqN2XBhAOP-WILTjfJMpXYCIstIfAAAAAU38sR4A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
