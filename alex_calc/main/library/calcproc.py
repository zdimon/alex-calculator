from datetime import datetime
import pandas as pd
from calendar import monthrange

class ThreeProcCalc():

    def __init__(self, data):
        self._data = data
        self._ostatok = data['sum']

    def get_month_range(self):
        return pd.date_range(self._data['date_start'],self._data['date_end'], 
              freq='MS').strftime("%Y-%m").tolist()

    def calc_sum_proc(self,sum, days):
        return round(((sum/100) * (self._data['proc']/365))*days,2)

    def count_total(self,report):
        sum = 0
        for item in report:
            sum += item['proc']
        return round(sum,2)

    def count_procent(self,report):
        for item in report:
            count_payments = len(item['payments'])
            item['sum_start'] = self._ostatok
            if count_payments>1:
                tmp_ostatok = self._ostatok
                tmp_summa = 0
                for index ,payment in enumerate(item['payments']):
                    print(item['month'],'---',count_payments,'---',index)
                    if index+1 == count_payments:
                        'последний платеж из двух'
                        print('last--', item['days'])
                        diff_after = datetime.strptime(item['end_date'], "%d/%m/%Y") - \
                                      datetime.strptime( payment['date'], "%d/%m/%Y")
                        self._ostatok = self._ostatok - payment['sum']
                        start_summa = self.calc_sum_proc(self._ostatok,diff_after.days)
                        item['proc'] = start_summa
                        item['repayment'] = item['repayment'] + payment['sum']
                        item['repl_date'] = payment['date']
                    elif index == 0:
                        'первый платеж из двух'
                        diff_before = datetime.strptime(payment['date'], "%d/%m/%Y") - \
                                      datetime.strptime( item['start_date'] , "%d/%m/%Y")
                        start_summa = self.calc_sum_proc(self._ostatok,diff_before.days)
                        next_payment = item['payments'][index+1]
                        diff = datetime.strptime(next_payment['date'], "%d/%m/%Y") - \
                               datetime.strptime(payment['date'], "%d/%m/%Y")
                        self._ostatok = self._ostatok - payment['sum']
                        end_summa = self.calc_sum_proc(self._ostatok,diff.days)
                        item['proc'] = start_summa + end_summa
                        item['repayment'] = item['repayment'] + payment['sum']
                        #print('first payment - ',start_summa, end_summa)
                      
                        print('have next--',next_payment['sum'],'diff-',diff)
            elif count_payments==1:
                'один платеж'
                day = item['payments'][0]['date'].split('/')[0]
                diff = item['days'] - int(day)
                summa_before = self.calc_sum_proc(self._ostatok,int(day))
                self._ostatok = self._ostatok - item['payments'][0]['sum']
                summa_after = self.calc_sum_proc(self._ostatok,diff)
                item['proc'] = summa_before + summa_after
                item['repayment'] = item['payments'][0]['sum']
                item['repl_date'] = item['payments'][0]['date']
                print (item['month'],'--one payment','day--',day,'diff=',diff)

            else:
                'нет платежей'
                summa = self.calc_sum_proc(self._ostatok,item['days'])
                item['proc'] = summa
                
                print(item['month'],'--no payments ost--', \
                     self._ostatok, 'days-', item['days'], \
                     'summa-',summa)
            item['ostatok'] = self._ostatok

    
    def calc_debt(self):
        monhts = self.get_month_range()
        report = []
        for month in monhts:
            y = month.split('-')[0]
            m = month.split('-')[1]
            days = monthrange(int(y), int(m))[1]
            record = {
                "month": month,
                "ostatok": 0,
                "proc": 0,
                "days": days,
                "payments": [],
                "start_date": '01/%s/%s' % (m, y),
                "end_date": '%s/%s/%s' % (days, m, y),
                "sum_start": 0,
                "repayment": 0,
                "repl_date": '---'
            }
            for item in self._data['payments']:
                iy = item['date'].split('/')[2]
                im = item['date'].split('/')[1]
                if im == m and iy == y:
                    record['payments'].append(item)
            report.append(record)
        self.count_procent(report)
        print(report)
        return report

    @staticmethod
    def count_days(start,end):
        start = datetime.strptime(start, "%d/%m/%Y")
        end = datetime.strptime(end, "%d/%m/%Y")
        return end - start

    def get_remains(self):
        remains = self._data['sum']
        for item in self._data['payments']:
            remains = remains - item["sum"]
        return remains

    def extract_pairs(self, payload):
        for index, item in enumerate(payload):
            if index == 0:
                start_date = self._data['date_start']
                end_date = payload[1][0]
                self._tmp_rimains = self._data['sum']
            elif index == len(payload)-1:
                start_date = payload[index][0]
                end_date = self._data['date_end']
                self._tmp_rimains = self._tmp_rimains - payload[index-1][1]
            else:
                start_date = payload[index][0]
                end_date = payload[index+1][0]
                self._tmp_rimains = self._tmp_rimains - payload[index-1][1]
            
            diff = self.count_days(start_date, end_date).days
            # sum = сумма кредита * 3% * кол-во дней просрочки / (365 или 366 или 360)
            fine = ((self._data['sum']/100) * (self._data['proc']/365))*diff

            yield [start_date, end_date, diff, self._tmp_rimains, round(fine,2)]

    def make_list(self):
        print(self._data['proc']/365)
        lst = []
        for p in data['payments']:
            lst.append([p['date'],p['sum']])
        res = [item for item in self.extract_pairs(lst)]
        return res

    def calc(self):
        print('Start')
        payment_list = self.make_list()
        out = {
                "ostatok": self.get_remains(),
                "history":  self.make_list()
              }
        return out




if __name__ == '__main__':
    data =     {
        "date_start": "01/01/2001",
        "date_end": "01/01/2002",
        "sum": 1000,
        "proc": 30,
        "payments": [
            {"date": "10/02/2001", "sum": 100},
            {"date": "25/02/2001", "sum": 150},
            {"date": "01/03/2001", "sum": 200},
            {"date": "01/04/2001", "sum": 300}
        ]
    }

    counter = ThreeProcCalc(data)
    counter.calc_debt()


    {
        'ostatok': 400, 
        'history': [
                    ['01/01/2001', '01/03/2001', 59, 1000, 4.85], 
                    ['01/03/2001', '01/04/2001', 31, 900, 2.55], 
                    ['01/04/2001', '01/01/2002', 275, 700, 22.6]
            ]
        }