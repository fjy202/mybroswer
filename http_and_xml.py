import copy
import re
def parse_http_response(response):
    res=response.split("\n")
    第一行=res[0]
    header="\n".join(res[1:]).split("\n\n")[0]
    header_dict={}
    for x in header.splitlines():
        header_dict[x.split(":")[0]]=x.split(":")[1]
    response_dict=copy.deepcopy(header_dict)
    version=第一行.split()[0]
    status=第一行.split()[1]
    response_dict["version"]=version
    response_dict["stat"]=status
    return response_dict
def parse_xml(html):
    