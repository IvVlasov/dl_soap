from requests import Session
from requests.auth import HTTPDigestAuth
from zeep import Client
from zeep.transports import Transport

session = Session()
session.auth = HTTPDigestAuth('demowebuser', 'Ax!761BN')
client = Client('https://services.fedresurs.ru/Bankruptcy/MessageServiceDemo/WebService.svc?WSDL',
                transport=Transport(session=session))

# res = client.service.GetMessageIds('2024-04-01T00:00:00')
# res = client.service.GetTradeMessages('2024-04-15T00:00:00')
# res = client.service.GetTradeMessagesByTrade(id='ОАЗФЦП-168',
#                                              startFrom='2024-04-15T00:00:00',
#                                              tradePlaceInn='7727752172')

# res = client.service.GetTradeMessageContent('5033901')
res = client.service.GetMessageContent('1663061')

# print(client.service.GetMessageContentResult(res))
print(res)
