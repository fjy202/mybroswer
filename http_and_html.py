import socket
import ssl
import copy
def parse_http_response(response):
    res=response.split("\n")
    第一行=res[0]
    header="\n".join("\n".join(res[1:]).split("\n\n")[0].splitlines()[1:])
    header_dict={}
    for x in header:
        header_dict[x.split(0)]=x.split(1)
    response_dict=copy.deepcopy(header_dict)
    version=第一行.split()[0]
    