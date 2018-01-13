
from xml_parser import get_root
from xml_validator import file_exists, is_valid_graph
import graph_repository

def process(file_name): 
    try:
        if file_exists(file_name):
            graph_xml = get_root(file_name)
            if is_valid_graph(graph_xml):
                graph_repository.add(graph_xml)
        else:
            print(file_name + " file does not exisit")
    except Exception as e:    
        #we can log any exception ex: logger.error('Failed to process : '+ str(e))
        print("sorry we are unable to process the request" + str(e))

if __name__ == '__main__':
    process("graph.xml")