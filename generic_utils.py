import datetime
import logging
import os

import requests


def index_generator(self, num_of_items):
    """
    Function to generate an item index for a ten minute period,
    i.e [0-9 mins].

    When you have a list of items and need to know which one
    will be chosen for xyz work for a ten-minute period at any
    time of day, this is useful.

    The generated index will be in the range [0, num of items-1]
    and will be determined by the current time of day (i.e. which
    tenth minute slot) and the number of items. Within that range,
    the indexes keep repeating themselves throughout the day.

    A day has a total of 1440 minutes. That means we have 144 ten-
    minute slots in a day [i.e. until time - 23:59], which means
    we can have a maximum of 143 indexes in a 0-based indexing.If
    the number of items exceeds 144, the function will run but will
    not generate indexes above 143.

    Example:

    You have five bundles for testing purpose. This function is
    useful if you want to know which bundle will be chosen for a
    specific ten-minute slot during the day.

    num_of_items = 5,
    now = 2022-03-23 11:21:52.935171,
    index = 68 % 5 = 3

    i.e. For the next ten minutes [11:20 - 11:29], the 3rd index bundle
    will be used for testing.

    :param num_of_items: total number of items. Range is [1-144]
    :type num_of_items: int

    :returns: the item's index for the current ten-minute period
    :rtype: int
    """

    now = datetime.datetime.now()
    num_of_min = now.hour * 60 + now.minute
    which_tenth_min = num_of_min // 10
    index = which_tenth_min % num_of_items
    return index


def post_asup_to_nsdiag(serial_number, dmp_dir, dmp_file, dmp_type, url, **kwargs):
    """
    Function to post tar bundles to the nsdiag server.
    Only tar bundles are accepted by the server.

    :param serial_number: new array name
    :param dmp_dir: path of the dump file
    :param dmp_file: dump filename
    :param dmp_type: asup type i.e. daily or statsstream
    :param url: nsdiag url
    :param kwargs: curl max time and cert options
    """

    max_time = kwargs.get("max_time", 7200)
    cert = kwargs.get("cert", None)
    dmp_data = os.path.join(dmp_dir, dmp_file)
    dmp_size = str(os.path.getsize(dmp_data))
    job_id = "0"

    print(dmp_data)

    headers = {
        "Nsdiag-Serial": serial_number,
        "Nsdiag-Size": dmp_size,
        "Nsdiag-Name": dmp_file,
        "Nsdiag-Type": dmp_type,
        "Nsdiag-Jobid": job_id,
    }

    try:
        logging.info("Posting to server")
        res = requests.post(
            url,
            headers=headers,
            data=open(dmp_data, "rb").read(),
            timeout=max_time,
            cert=cert,
        )
    except Exception as e:
        logging.error(e)
        logging.info("Error on posting to NSdiag")
        print("failed")
    else:
        if res:
            print(res.status_code)
            print(res.content)
            logging.info("Successfully posted to NSdiag")
            print("Success")
        else:
            logging.info("Error on posting to NSdiag")
            print("failed")
