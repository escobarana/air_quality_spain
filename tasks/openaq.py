from celery import shared_task
from crawler.wrappers.opeanaqapi import OpenaqAuthWrapper
from writers.openaq import save_measures
from django.conf import settings
import logging

logger_obj = logging.getLogger(__name__)

api_name_const = 'OpenAQ API: '


@shared_task(autoretry_for=(Exception,), max_retries=settings.MAX_RETRIES, exponential_backoff=2, retry_jitter=True)
def get_measures_september_2021(rows_loaded: int = 0, page: int = 1) -> dict:
    """
        Task function to load all data measures from september 2021 in the MongoDB database
    :param  rows_loaded: Number of rows loaded on previous iterations
    :param  page: Current page number
    :return: Dictionary containing the status of the task (success or error) and related message
    """
    try:
        logger_obj.info(f'{api_name_const}: Starting new measures september 2021 view task')
        measures = OpenaqAuthWrapper().openaq.get_measurements_2021(page=page)

        if len(measures['data']) > 0:
            save_measures(data=measures['data'])
        else:
            logger_obj.info(f'{api_name_const}: get_measures_september_2021: No available data')

        # Counting rows
        rows_loaded += measures['current_count']

        # Storing next page
        next_page = measures['next_page']

        if next_page:
            # Paginate
            get_measures_september_2021.apply_async(kwargs={"page": next_page,
                                                            "rows_loaded": rows_loaded},
                                                    priority=9)

        else:
            logger_obj.info(
                f'{api_name_const}: get_measures_september_2021: There are no more pages, '
                f'total pages retrieved: {page}')

        # Log results and return
        result_message = f'{api_name_const}: get_measures_september_2021: Page: {page} finished'
        logger_obj.info(result_message)
        return {'status': 'success', 'message': result_message}

    except Exception as e:
        status_detail = f"{str(e.__class__.__name__)}: {e}"
        return {'status': 'error', 'message': api_name_const + ': ' + status_detail}


@shared_task(autoretry_for=(Exception,), max_retries=settings.MAX_RETRIES, exponential_backoff=2, retry_jitter=True)
def get_measures_september_2022(rows_loaded: int = 0, page: int = 1) -> dict:
    """
        Task function to load all data measures from september 2022 in the MongoDB database
    :param  rows_loaded: Number of rows loaded on previous iterations
    :param  page: Current page number
    :return: Dictionary containing the status of the task (success or error) and related message
    """
    try:
        logger_obj.info(f'{api_name_const}: Starting new measures september 2022 view task')
        measures = OpenaqAuthWrapper().openaq.get_measurements_2022(page=page)

        if len(measures['data']) > 0:
            save_measures(data=measures['data'])
        else:
            logger_obj.info(f'{api_name_const}: get_measures_september_2022: No available data')

        # Counting rows
        rows_loaded += measures['current_count']

        # Storing next page
        next_page = measures['next_page']

        if next_page:
            # Paginate
            get_measures_september_2021.apply_async(kwargs={"page": next_page,
                                                            "rows_loaded": rows_loaded},
                                                    priority=9)

        else:
            logger_obj.info(
                f'{api_name_const}: get_measures_september_2022: There are no more pages, '
                f'total pages retrieved: {page}')

        # Log results and return
        result_message = f'{api_name_const}: get_measures_september_2022: Page: {page} finished'
        logger_obj.info(result_message)
        return {'status': 'success', 'message': result_message}

    except Exception as e:
        status_detail = f"{str(e.__class__.__name__)}: {e}"
        return {'status': 'error', 'message': api_name_const + ': ' + status_detail}
