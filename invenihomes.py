import requests
import json

cookies = {
    "ASP.NET_SessionId": "wqtlhq4xc4i3jwp5o5dw35kl",
    "cookiesession1": "678A3E4ADFDAAADC3A172507D5E2CAAA",
    "Pl.userlang": "eng",
    "offset": "-300",
    "stdtimezoneoffset": "-300",
    "clientdstoffset": "0",
    "clienttz": "Asia%2FKarachi",
    "DisplayDivasCookiesBanner": "yes",
    "Cookie Management": '{"declined":"","all":"Cookie Management,DisplayDivasCookiesBanner,DisplayDivasCookiesBanner,Pl.userlang,clientdstoffset,clienttz,cookiesession1,dl_row_count,offset,stdtimezoneoffset","accept_all":"true","last_checked":""}',
    ".ASPXAUTH": "EB83A419889F9B92000018DB4652549EBFAE15FD1E66031067C80BA8C3804F3305DCAABF4AB5D47B7C6EDFA40B295C012FBA796517BDC1ABD331AE6741935EEC999E1FA4295062B02D5CD69500D7B4260414A3EE77D1323A0246D41BF405AA5E88CC09C9B3BFC23066BD183040D96E5FC5726D98B51C00B688293E5DB3F77F3F",
    "_ga": "GA1.1.75901916.1681572384",
    "_ga_NQGSYX1FS4": "GS1.1.1681577015.2.0.1681577015.0.0.0",
}

headers = {
    "authority": "portal.inveniohomes.com",
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # 'cookie': 'ASP.NET_SessionId=wqtlhq4xc4i3jwp5o5dw35kl; cookiesession1=678A3E4ADFDAAADC3A172507D5E2CAAA; Pl.userlang=eng; offset=-300; stdtimezoneoffset=-300; clientdstoffset=0; clienttz=Asia%2FKarachi; DisplayDivasCookiesBanner=yes; Cookie Management={"declined":"","all":"Cookie Management,DisplayDivasCookiesBanner,DisplayDivasCookiesBanner,Pl.userlang,clientdstoffset,clienttz,cookiesession1,dl_row_count,offset,stdtimezoneoffset","accept_all":"true","last_checked":""}; .ASPXAUTH=EB83A419889F9B92000018DB4652549EBFAE15FD1E66031067C80BA8C3804F3305DCAABF4AB5D47B7C6EDFA40B295C012FBA796517BDC1ABD331AE6741935EEC999E1FA4295062B02D5CD69500D7B4260414A3EE77D1323A0246D41BF405AA5E88CC09C9B3BFC23066BD183040D96E5FC5726D98B51C00B688293E5DB3F77F3F; _ga=GA1.1.75901916.1681572384; _ga_NQGSYX1FS4=GS1.1.1681572383.1.1.1681572895.0.0.0',
    "origin": "https://portal.inveniohomes.com",
    "referer": "https://portal.inveniohomes.com/",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.906 (beta) Yowser/2.5 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

data = {
    "document_no": "307",
    "attrib_code": "307_bp_tile",
    "parms": 'arg1=[{"search_limit":"52","search_id":"","on_behalf":"8193","page_number":"1","sort_order":"villa_price~DESC","destination":"RGMYKONOS","license_options":"null","min_bedrooms":"1","max_bedrooms":"20","numberof_guests":"1","availability":"100"}]',
    "er_code": "",
}

response = requests.post(
    "https://portal.inveniohomes.com/contentloader/CallDBMethod?source=actions/method_type&type=db&name=search",
    cookies=cookies,
    headers=headers,
    data=data,
)

data = []

s_json = response.json()
json_bloc = json.loads(s_json)
for d in json_bloc[0]["result"]:
    try:
        loc = d["geolocation"]
    except:
        loc = "N/A"
    data.append(
        {
            "Guests": d["guests"],
            "Rooms": d["bedrooms"],
            "Bathrooms": d["bathrooms"],
            "Short_Description": d["tagline"],
            "Price": d["villa_price"],
            "Location": loc,
            "City": d["city"],
        }
    )
with open("inveniohomes.json", "w") as jf:
    jf.write(json.dumps(data, indent=2))
# print(response.json())

# url = "https://portal.inveniohomes.com/contentloader/CallDBMethod?source=actions/method_type&type=db&name=search"


# def homes_listing():
#     data = []

#     response = requests.post(url, cookies=cookies, headers=headers, data=data)
#     print(response.text)
#     # s_json = response.json()
#     # print(s_json)
#     # json_bloc = json.loads(s_json)
#     # print(json_bloc[0]["result"])

#     # for d in json_bloc[0]["result"]:
#     #     data.append(
#     #         {
#     #             "Guests": d["guests"],
#     #             "Rooms": d["bedrooms"],
#     #             "Bathrooms": d["bathrooms"],
#     #             "Short_Description": d["tagline"],
#     #             "Price": d["villa_price"],
#     #             "Location": d["geoloaction"],
#     #             "City": d["city"],
#     #         }
#     #     )
#     # with open("inveniohoes.json", "w") as jf:
#     #     jf.write(json.dumps(data))
#     # return data


# if __name__ == "__main__":
#     data = homes_listing()
