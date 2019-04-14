import socket
import ssl
def parse_http_response(response):
    res=response.split("\n")
    第一行=res[0]
    header="\n".join(res[1:]).split("\n\n")[0]
    header_dict={}
    for x in header:
        header_dict[x.split(0)]=x.split(1)
    