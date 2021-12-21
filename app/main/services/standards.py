class Output():
    def __init__(self):
        pass

    def response_api(self, code, data):
        codes_messages = {
            200: "Success!",
            400: "Bad request.",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Data don't founded!",
            500: "Internal server error!",
            502: "Bad Gateway"
        }
        if code in codes_messages.keys():
            msg = codes_messages[code]
        else:
            msg = 'Error!!'
            code = 404
        if type(data) != list:
            data = [data]
        response = {'message': msg, 'results': data, 'status': code}, code
        return response

    def return_funtion(self, code, data):
        response = {'results': data, 'status': code}
        return response