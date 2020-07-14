# _*_ coding: utf-8 _*_

from flask import jsonify

from .messages import (
        MSG_INVALID_DATA, MSG_DOES_NOT_EXIST, MSG_ALREADY_EXISTS,
        MSG_RESOURCE_MUST_STRING, MSG_EXCEPTION)

def resp_data_invalid(resource :str, errors :dict, 
                      msg :str = MSG_INVALID_DATA):
    """
    Responses 422 - Unprocessable Entity
    """

    if not isinstance(resource, str):
        raise ValueError(MSG_RESOURCE_MUST_STRING)

    resp = jsonify({
        "resource" : resource,
        "message": msg,
        "errors": errors,
    })

    resp.status_code = 422
    return resp

def resp_exception(resource: str, description :str = "", 
                   msg=MSG_EXCEPTION):
    """
    Response 500
    """

    if not isinstance(resource, str):
        raise ValuerError(MSG_RESOURCE_MUST_STRING)

    resp = jsonify({
        "resource": resource,
        "message": msg,
        "description": description
    })

    resp.status_code = 500

    return resp

def resp_does_not_exist(resource :str, description :str=None, msg=None):
    """
    Responses 404 - Not Found
    """

    if not isinstance(resource, str):
        raise ValueError(MSG_RESOURCE_MUST_STRING)

    if not msg:
        msg = MSG_DOES_NOT_EXIST.format(description)
    else: 
        msg = msg.format(description)

    resp = jsonify({
        "resource": resource,
        "message": msg 
    })

    resp.status_code = 404
    
    return resp

def resp_already_exists(resource :str, description :str):
    """
    Responses 400
    """

    if not isinstance(resource, str):
        raise ValueError(MSG_RESOURCE_MUST_STRING)

    resp = jsonify({
        "resource": resource,
        "message": MSG_ALREADY_EXISTS.format(description),
    })

    resp.status_code = 400

    return resp

def resp_ok(resource :str, msg :str, data=None, **extras):
    """
    Response 200 - Success
    """

    response = {
        "status": 200,
        "message": msg,
        "resource": resource
    }

    if data:
        response["data"] = data

    response.update(extras)

    resp = jsonify(response)

    resp.status_code = 200

    return resp

def resp_ok_no_content():
    """
    Response 204 - No Content
    Used in response to delete operation
    """

    resp = jsonify()
    resp.status_code = 204

    return resp
