import azure.functions as func
import json
from .cpf_utils import validar_cpf

def main(req: func.HttpRequest) -> func.HttpResponse:
    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpResponse(
                json.dumps({"erro": "CPF não informado"}),
                mimetype="application/json",
                status_code=400
            )
        else:
            cpf = req_body.get('cpf')

    if not cpf:
        return func.HttpResponse(
            json.dumps({"erro": "CPF não informado"}),
            mimetype="application/json",
            status_code=400
        )

    valido = validar_cpf(cpf)

    return func.HttpResponse(
        json.dumps({"cpf": cpf, "valido": valido}),
        mimetype="application/json",
        status_code=200 if valido else 400
    )
