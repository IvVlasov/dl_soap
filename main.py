from requests import Session
from requests.auth import HTTPDigestAuth
from zeep import Client
from zeep.transports import Transport
import json
from datetime import timedelta, datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse, isoparse


session = Session()
session.auth = HTTPDigestAuth('demowebuser', 'Ax!761BN')
client = Client('https://services.fedresurs.ru/Bankruptcy/MessageServiceDemo/WebService.svc?WSDL',
                transport=Transport(session=session))


def _save(name, data):
    with open(f'data/{name}', 'w') as f:
        f.write(str(data))


def _get_event_time(data, _type):
    soup = BeautifulSoup(data, 'xml')
    _type = 'BiddingProcessInfo' if _type == 'BiddingProcess' else _type
    msg = soup.find(_type)
    return msg['EventTime']


def _get_id(data):
    soup = BeautifulSoup(data, 'xml')
    msg = soup.find('IDEFRSB')
    return msg.text


def GetMessageContent(ident):
    res = client.service.GetMessageContent(ident)
    _save('GetMessageContent.xml', res)
    return res


def GetTradeMessageContent(ident):
    res = client.service.GetTradeMessageContent(ident)
    _save('GetTradeMessageContent.xml', res)
    return res


def GetTradeMessages():
    start = datetime(2023, 1, 23)
    end = start + timedelta(days=1)
    res = client.service.GetTradeMessages(startFrom=start.strftime('%Y-%m-%dT%H:%M:%S'),
                                          endTo=end.strftime('%Y-%m-%dT%H:%M:%S'))
    _save('GetTradeMessages.json', res)
    return res


# a = {
#                     'TradeMessage': [
#                         {
#                             'ID': 4930590,
#                             'GUID': '3232c647-7347-4089-b6d4-0c4c2129875c',
#                             'Type': 'BiddingInvitation'
#                         },
#                         {
#                             'ID': 4930591,
#                             'GUID': 'd1d2b70a-d697-4d4e-a7f9-4f714390e782',
#                             'Type': 'ApplicationSessionStart'
#                         },
#                         {
#                             'ID': 4930592,
#                             'GUID': '18ba98f0-1eb5-42fd-b593-f88fc8bb0efc',
#                             'Type': 'ApplicationSessionEnd'
#                         },
#                         {
#                             'ID': 4930598,
#                             'GUID': '9f39f966-e3db-403b-8d14-4e5245132e1e',
#                             'Type': 'BiddingFail'
#                         },
#                         {
#                             'ID': 4930599,
#                             'GUID': '0639ff16-9950-4bcf-8114-2a0147a10231',
#                             'Type': 'ApplicationSessionStatistic'
#                         },
#                         {
#                             'ID': 4930600,
#                             'GUID': '16ed4314-bddc-476a-b9a7-da0f3024672d',
#                             'Type': 'ContractSale'
#                         }
#                     ]
#                 }


# res = GetTradeMessages()
# for etp in res:
#     trades = etp['TradeList']['Trade']
#     for trade in trades:

# msgs = a['TradeMessage']
# for msg in msgs:
#     _type = msg['Type']
#     res = GetTradeMessageContent(msg['ID'])
#     ident = _get_id(res)

#     print(GetMessageContent(ident))
#     # _save(_type + '.xml', res)

#     # time = _get_event_time(res, _type)
#     # print(isoparse(time))


# TEST 2
# res = GetTradeMessageContent(4930590)
# soup = BeautifulSoup(res, 'xml')
# lot_list = soup.find('LotList').find_all('Lot')
# # print(lot_list, type(lot_list))

# for lot in lot_list:
#     # print(lot)
#     print(lot.has_attr('StartPrice'))

# ident = _get_id(res)
# print(GetMessageContent(1667294))

# TEST 3
r = GetTradeMessageContent(4930605)
soup = BeautifulSoup(r, 'xml')
print(soup.find('ArbitrManager').name)

# GetMessageContent(1667294)
