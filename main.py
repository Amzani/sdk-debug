import datetime
import os
from dotenv import load_dotenv

import apideck
from apideck.api import accounting_api
from apideck.model.allocation import Allocation
from apideck.model.bill_payment import BillPayment
from apideck.model.currency import Currency
from apideck.model.linked_ledger_account import LinkedLedgerAccount
from apideck.model.linked_supplier import LinkedSupplier
import pprint


# Load environment variables from .env file
load_dotenv()


# Load environment variables
CONSUMER_ID = os.getenv('CONSUMER_ID')
APP_ID      = os.getenv('APP_ID')
API_KEY     = os.getenv('API_KEY')
HOST        = os.getenv('HOST')

if not all([CONSUMER_ID, APP_ID, API_KEY, HOST]):
    raise ValueError("Missing required environment variables. Please check your .env file.")


configuration = apideck.Configuration(
   host = HOST
)
configuration.api_key['apiKey'] = API_KEY
configuration.api_key_prefix['apiKey'] = 'Bearer'

with apideck.ApiClient(configuration) as api_client:
  api_instance = accounting_api.AccountingApi(api_client)

  try:
    all_bills = api_instance.bills_all(
      consumer_id=CONSUMER_ID,
      app_id=APP_ID
    )
    pprint.pprint(all_bills)

    payment_data = BillPayment(**{
        "currency": Currency("GBP"),
        "currency_rate": 1.0,
        "total_amount": 24.36,
        "transaction_date": datetime.datetime.now(),
        "supplier": LinkedSupplier(id="56"),
        "account": LinkedLedgerAccount(id="35"),
        "allocations": [Allocation(**{"id": "472", "type": "bill", "amount": 24.36})],
        "row_version": "0",
        "payment_method": "CreditCard"
      })
    
    api_response = api_instance.bill_payments_add(
      bill_payment=payment_data,
      consumer_id=CONSUMER_ID,
      app_id=APP_ID
    )
    pprint.pprint(api_response)

  except apideck.ApiException as e:
     print("Exception when calling AccountApi->bill_all %s\n" % e)