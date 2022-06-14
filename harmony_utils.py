import requests
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder


def post_upload_server_v3(url, file_path, file_domain, file_type, file_size, file_uuid, meta_sn):
    """
    Function used to perform a HTTP POST operation to Upload Server Component on Harmony Platform

    :param url: hosted url of the upload server component
    :param file_path: absolute path where the file bundle resides
    :param file_type: type of the file being uploaded ex:metrics, config
    :param file_uuid: id to uniquely identify ingested bundle on the pipeline ex: regex of timestamp_asupid
    :param file_size: size indicating the size in bytes of the bundles that is being uploaded
    :param file_domain: type of file For instance: appinsights, nimble etc.,
    :param meta_sn: device ID for the gateway VM.
    :return: response from upload server on success with a HTTP status code 200
             response includes bucket_name, key, location and an e-tag
    """

    m = MultipartEncoder(
        fields={
            'file': ('filename', open(file_path, 'rb'))
        }
    )
    response = requests.post(url, data=m,
                             headers={
                                 'Content-Type': m.content_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILEDOMAIN': file_domain,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILETYPE': file_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-BLIND-FILE-UUID': file_uuid,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILESIZE': file_size,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-SN': meta_sn
                             })
    return response

def post_upload_server_v2(url, file_path, file_domain, file_type, file_size, file_uuid):
    """
    Function used to perform a HTTP POST operation to Upload Server Component on Harmony Platform

    :param url: hosted url of the upload server component
    :param file_path: absolute path where the file bundle resides
    :param file_type: type of the file being uploaded ex:metrics, config
    :param file_uuid: id to uniquely identify ingested bundle on the pipeline ex: regex of timestamp_asupid
    :param file_size: size indicating the size in bytes of the bundles that is being uploaded
    :param file_domain: type of file For instance: appinsights, nimble etc.,
    :return: response from upload server on success with a HTTP status code 200
             response includes bucket_name, key, location and an e-tag
    """

    m = MultipartEncoder(
        fields={
            'file': ('filename', open(file_path, 'rb'))
        }
    )
    response = requests.post(url, data=m,
                             headers={
                                 'Content-Type': m.content_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILEDOMAIN': file_domain,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILETYPE': file_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-BLIND-FILE-UUID': file_uuid,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILESIZE': file_size
                             })
    return response


def post_upload_server(url, file_path, file_type, file_subtype, file_uuid):
    """
    Function used to perform a HTTP POST operation to Upload Server Component on Harmony Platform

    :param url: hosted url of the upload server component
    :param file_path: absolute path where the file bundle resides
    :param file_type: type of the file being uploaded ex:metrics, config
    :param file_uuid: id to uniquely identify ingested bundle on the pipeline ex: regex of timestamp_asupid
    :param file_subtype: subtype of the file for instance: statsstream, configstream
    :return: response from upload server on success with a HTTP status code 200
             response includes bucket_name, key, location and an e-tag
    """

    m = MultipartEncoder(
        fields={
            'file': ('filename', open(file_path, 'rb'))
        }
    )
    response = requests.post(url, data=m,
                             headers={
                                 'Content-Type': m.content_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILETYPE': file_type,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-FILESUBTYPE': file_subtype,
                                 'X-INFOSIGHT-UPLOAD-SERVER-META-BLIND-FILE-UUID': file_uuid
                             })
    return response
