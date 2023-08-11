from datetime import datetime, timedelta
from calendar import monthrange
from collections import OrderedDict

class ThreeProcCalc():

    def __init__(self, data):
        self._data = data
        self._ostatok = data['sum']

    def get_month_range(self):
        dates = [self._data['date_start'], self._data['date_end']]
        start, end = [datetime.strptime(_, "%d/%m/%Y") for _ in dates]
        return list(OrderedDict(((start + timedelta(_)).strftime(r"%Y-%m"), None) for _ in range((end - start).days)).keys())

    def calc_sum_proc(self,sum, days):
        return round(((sum/100) * (self._data['proc']/365))*days,2)

    def count_total(self,report):
        sum = 0
        for item in report:
            sum += item['proc']
        return round(sum,2)
    
    @staticmethod
    def month_verb(date):
        m = int(date.split('-')[1])
        y = date.split('-')[0]
        if m==1:
            return '%s %s' % ('Январь',y)
        elif m ==2:
            return '%s %s' % ('Февраль',y)
        elif m ==3:
            return '%s %s' % ('Март',y)
        elif m ==4:
            return '%s %s' % ('Апрель',y)
        elif m ==5:
            return '%s %s' % ('Май',y)
        elif m ==6:
            return '%s %s' % ('Июнь',y)
        elif m ==7:
            return '%s %s' % ('Июль',y)
        elif m ==8:
            return '%s %s' % ('Август',y)
        elif m ==9:
            return '%s %s' % ('Сентябрь',y)
        elif m ==10:
            return '%s %s' % ('Октябрь',y)
        elif m ==11:
            return '%s %s' % ('Ноябрь',y)
        elif m ==12:
            return '%s %s' % ('Декабрь',y)
        return 'неизвестно %s' % m

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

    
    def make_report(self):
        monhts = self.get_month_range()
        report = []
        for month in monhts:
            y = month.split('-')[0]
            m = month.split('-')[1]
            days = monthrange(int(y), int(m))[1]
            print(monthrange(int(y), int(m)), '999999999', month)
            record = {
                "month": month,
                "month_verb": self.month_verb(month),
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
    counter.make_report()
