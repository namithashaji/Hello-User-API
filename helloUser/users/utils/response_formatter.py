def success_response(data=None, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(error, message="Error"):
    return {
        "status": "error",
        "message": message,
        "error": error
    }
