"""Testes de integração para o cliente da API Nager.Date.

Usamos a biblioteca `responses` para mockar respostas HTTP, garantindo que:
- Nenhuma requisição real à internet é feita durante o CI.
- Os cenários de falha (404, timeout, JSON inválido) são testados de forma determinística.
"""
import pytest
import requests
import responses

from devtodo.api import URL_BASE, listar_feriados
from devtodo.core import DevtodoError


@responses.activate
def test_listar_feriados_sucesso():
    responses.add(
        responses.GET,
        f"{URL_BASE}/2025/BR",
        json=[
            {
                "date": "2025-01-01",
                "localName": "Confraternização Universal",
                "name": "New Year's Day",
                "countryCode": "BR",
            },
            {
                "date": "2025-04-21",
                "localName": "Tiradentes",
                "name": "Tiradentes' Day",
                "countryCode": "BR",
            },
        ],
        status=200,
    )
    result = listar_feriados(2025, "BR")
    assert len(result) == 2
    assert result[0]["localName"] == "Confraternização Universal"
    assert result[1]["date"] == "2025-04-21"


@responses.activate
def test_listar_feriados_pais_invalido_404():
    responses.add(responses.GET, f"{URL_BASE}/2025/XX", status=404)
    with pytest.raises(DevtodoError, match="não encontrado"):
        listar_feriados(2025, "XX")


@responses.activate
def test_listar_feriados_timeout():
    responses.add(
        responses.GET,
        f"{URL_BASE}/2025/BR",
        body=requests.Timeout("simulado"),
    )
    with pytest.raises(DevtodoError, match="Timeout"):
        listar_feriados(2025, "BR")


@responses.activate
def test_listar_feriados_json_invalido():
    responses.add(
        responses.GET,
        f"{URL_BASE}/2025/BR",
        body="<html>not json</html>",
        status=200,
        content_type="text/html",
    )
    with pytest.raises(DevtodoError, match="JSON"):
        listar_feriados(2025, "BR")
