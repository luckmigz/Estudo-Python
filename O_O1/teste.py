from conta import Conta
from Data import Data

conta = Conta(123,"John",5.55,1000)
conta1 = Conta(123,"Faster",5.55,1000)
conta.extrato()
d = Data(21,11,2007)
d.format()
conta1.transfere(5.00,conta)
conta1.extrato()
conta.extrato()