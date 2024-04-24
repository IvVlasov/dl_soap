from zeep import Client

client = Client('https://services.fedresurs.ru/Bankruptcy/MessageServiceDemo/WebService.svc?WDSL')
result = client.service.ConvertSpeed(
    100, 'kilometersPerhour', 'milesPerhour')

# assert result == 62.137
