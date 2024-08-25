from requests import Session
from requests.auth import HTTPDigestAuth
from zeep import Client
from zeep.transports import Transport
import json
# import xmltodict, json
from bs4 import BeautifulSoup
import html 
from datetime import date, timedelta, datetime


session = Session()
session.auth = HTTPDigestAuth('demowebuser', 'Ax!761BN')
client = Client('https://services.fedresurs.ru/Bankruptcy/MessageServiceDemo/WebService.svc?WSDL',
                transport=Transport(session=session))


def GetSroRegister():
    res = client.service.GetArbitrManagerRegister()
    with open('GetArbitrManagerRegister.json', 'w') as f:
        f.write(str(res))
# GetSroRegister()


def GetMessageContent(ident):
    res = client.service.GetMessageContent(ident)
    with open('GetMessageContent.xml', 'w') as f:
        f.write(str(res))


# def GetDebtorByIdBankrupt(idBankrupt):

def SearchDebtorByCode(value):
    res = client.service.SearchDebtorByCode('CompanyInn', value)
    with open('SearchDebtorByCode.json', 'w') as f:
        f.write(str(res))


def GetCompanyTradeOrganizerRegister():
    res = client.service.GetCompanyTradeOrganizerRegister()
    with open('GetCompanyTradeOrganizerRegister.json', 'w') as f:
        f.write(str(res))


def GetTradeMessageContent(ident):
    res = client.service.GetTradeMessageContent(ident)
    with open('GetTradeMessageContent.xml', 'w') as f:
        f.write(str(res))
    return res




def GetDebtorMessagesContentForPeriodByIdBankrupt():
    res = client.service.GetDebtorMessagesContentForPeriodByIdBankrupt(idBankrupt=138895)
    with open('GetDebtorMessagesContentForPeriodByIdBankrupt.xml', 'w') as f:
        f.write(str(res))
# GetDebtorMessagesContentForPeriodByIdBankrupt()


def GetDebtorRegister(start):
    res = client.service.GetDebtorRegister(date=start.strftime('%Y-%m-%dT%H:%M:%S'))
    # return res
    with open('GetDebtorRegister.json', 'w') as f:
        f.write(str(res))



# start = datetime(2011, 1, 1)
# while start < datetime.now():
# res = GetDebtorRegister(start)
# start = start + timedelta(days=100)

# print(start)
# if not res:
#     continue

# print(len(res['_value_1']))


def GetTradeMessages(start):
    # end = start + timedelta(days=1)
    end = start + timedelta(days=10)
    res = client.service.GetTradeMessages(startFrom=start.strftime('%Y-%m-%dT%H:%M:%S'),
                                          endTo=end.strftime('%Y-%m-%dT%H:%M:%S'))
    with open('GetTradeMessages.json', 'w') as f:
        f.write(str(res))
    return res


def test_all_messages():
    start = datetime(2021, 4, 20)
    while start < datetime.now():
        trade_messages = GetTradeMessages(start)
        if not trade_messages:
            continue

        for msg in trade_messages[0]['TradeList']['Trade'][0]['MessageList']['TradeMessage']:
            if msg['Type'] == 'BiddingDeclaration':
                print(start)
        start = start + timedelta(days=10)

# test_all_messages()


def get_lots_info(msg, bidd_lots):
    soup = BeautifulSoup(html.unescape(msg), 'xml')
    lot_table = soup.find('LotTable').find_all('AuctionLot')
    for lot in lot_table:
        lot_num = lot.find('Order').text
        if lot_num not in bidd_lots.keys():
            continue
        bidd_lots[lot_num]['name'] = lot.find('Description').text
        bidd_lots[lot_num]['start_price'] = lot.find('StartPrice').text
    return bidd_lots


# res = GetTradeMessageContent(5033699)
# soup = BeautifulSoup(res, 'xml')
# arbitr = soup.find('ArbitrManager')
# print(arbitr.get('SROName', ''))

# GetMessageContent(1666968)

# start = datetime(2024, 1, 30)
# GetTradeMessages(start)


# GetTradeMessageContent(4930585)


# GetDebtorRegister()

# def test(ident):
#     res = client.service.GetTradeMessageContent(ident)

# test(5033871)



# GetMessageContent(1668375)
# GetTradeMessageContent(5033200)
# SearchDebtorByCode(5709003233)


# name = trade_message["soap:Envelope"]["soap:Body"]["SetBiddingInvitation"]["BiddingInvitation"]["TradeInfo"]


# GetMessageContent(1670258)


# res = client.service.GetMessageIds('2024-01-01T00:00:00')
# print(res)

# res = client.service.GetTradeMessagesByTrade(id='142247',
#                                              startFrom='2024-04-15T00:00:00',
#                                              tradePlaceInn='7708514824')

# res = client.service.GetTradeMessages('1663061')

# print(client.service.GetMessageContentResult(res))
# print(client.service.GetTradeMessagesByTrade(142247))
# GetCompanyTradeOrganizerRegister()
# GetMessageContent(1663061)
# GetTradeMessageContent(5033893)
