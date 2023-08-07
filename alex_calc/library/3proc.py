from datetime import datetime

class ThreeProcCalc():

    def __init__(self, data):
        self._data = data

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
        "proc": 3,
        "payments": [
            {"date": "01/02/2001", "sum": 100},
            {"date": "01/03/2001", "sum": 200},
            {"date": "01/04/2001", "sum": 300}
        ]
    }

    counter = ThreeProcCalc(data)
    print(counter.calc())