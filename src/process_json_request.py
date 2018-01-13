
from json_input import get_json_queries
from json_parser import get_queries
from response import get_response


def process():
    try:
        queries = get_json_queries()
        response = get_response(queries)
        return response

    except Exception as e:    
        #we can log any exception ex: logger.error('Failed to process : '+ str(e))
        print("sorry we are unable to process the request ")

if __name__ == '__main__':
    process()
