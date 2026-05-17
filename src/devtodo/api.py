"""Cliente HTTP para integração com a API pública Nager.Date."""
import requests

from devtodo.core import DevtodoError

URL_BASE = "https://date.nager.at/api/v3/PublicHolidays"
TIMEOUT = 10


def listar_feriados(ano: int, pais: str) -> list[dict]:
    """Busca feriados públicos de um país/ano via Nager.Date.

    Retorna lista de dicts com chaves: date, localName, name, countryCode.
    Lança DevtodoError em qualquer falha (HTTP, timeout, JSON inválido).
    """
    url = f"{URL_BASE}/{ano}/{pais.upper()}"
    try:
        resp = requests.get(url, timeout=TIMEOUT)
    except requests.Timeout as e:
        raise DevtodoError(f"Timeout ao consultar feriados: {e}") from e
    except requests.ConnectionError as e:
        raise DevtodoError(f"Falha de conexão: {e}") from e

    if resp.status_code == 404:
        raise DevtodoError(f"País '{pais}' não encontrado ou sem dados para {ano}.")
    if resp.status_code != 200:
        raise DevtodoError(f"Erro HTTP {resp.status_code} ao consultar feriados.")

    try:
        return resp.json()
    except ValueError as e:
        raise DevtodoError("Resposta da API não é JSON válido.") from e
