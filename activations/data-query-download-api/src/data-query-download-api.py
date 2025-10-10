# Requisição de dados de um objeto de dados
import json
import csv
import requests

# Configurações de autenticação para obter o primeiro token
auth_url = "https://login.salesforce.com/services/oauth2/token"
client_id = "[SEU_CLIENT_ID]"
client_secret = "[SEU_CLIENT_SECRET]"
username = "[SEU_USUARIO]"
password = "[SUA_SENHA]"

base_url = "[URL_DE_ACESSO]"
query_endpoint = "/services/a360/token"
query = "SELECT * FROM Individual__dll"
base_uri = "https://SUA_INSTANCIA_URL.c360a.salesforce.com/api/v2/query"


def get_initial_token():
    auth_data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(auth_url, data=auth_data, headers=headers)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Erro ao obter o primeiro token: {response.status_code} - {response.text}")


def get_customer_360_token(access_token):
    query_url = f"{base_url}{query_endpoint}"
    payload = {
        "grant_type": "urn:salesforce:grant-type:external:cdp",
        "subject_token": access_token,
        "subject_token_type": "urn:ietf:params:oauth:token-type:access_token"
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(query_url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Erro ao obter o token do Customer 360: {response.status_code} - {response.text}")


def query_customer_360_audiences(customer_360_token):
    query_url = f"{base_uri}"
    payload = {"sql": query}
    headers = {
        "Authorization": f"Bearer {customer_360_token}",
        "Content-Type": "application/json"
    }

    all_data = []
    next_batch_id = None

    while True:
        if not next_batch_id:
            # Primeira requisição (POST)
            response = requests.post(query_url, headers=headers, json=payload)
        else:
            # Requisições subsequentes (GET)
            response = requests.get(f"{base_uri}/{next_batch_id}", headers=headers)

        if response.status_code == 200:
            result = response.json()
            data = result.get("data", [])
            all_data.extend(data)

            # Verifica se há mais batches para processar
            next_batch_id = result.get("nextBatchId")
            if not next_batch_id:
                break
        else:
            raise Exception(f"Erro ao executar a consulta: {response.status_code} - {response.text}")

    # Salva todos os dados acumulados em um CSV
    save_data_to_csv(all_data)


def save_data_to_csv(data):
    file_name = "insight_calculado_rfv_fev_2025_final.csv"

    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Arquivo CSV salvo com sucesso: {file_name}")
    except Exception as e:
        raise Exception(f"Erro ao salvar o arquivo CSV: {e}")


def main():
    try:
        access_token = get_initial_token()
        customer_360_token = get_customer_360_token(access_token)
        query_customer_360_audiences(customer_360_token)
        print("Processo concluído com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()